from dataclasses import dataclass
from typing import List, Set, Tuple
import random, os, csv, shutil


OUTPUT_METADATA = '/home/piotr/Dresden/ms-dis-nmr-experiments/dependencies/instances/instances_metadata.csv'
OUTPUT_INSTANCES_MSDIS = '/home/piotr/Dresden/ms-dis-nmr-experiments/dependencies/instances/ms-dis'
OUTPUT_INSTANCES_NMSL = '/home/piotr/Dresden/ms-dis-nmr-experiments/dependencies/instances/nm-s4f-sl'


@dataclass
class SLPRule:
    standpoint: str
    head: str
    pos_body: List[str]   # p_1..p_m
    neg_body: List[str]   # p_{m+1}..p_{m+n}


@dataclass
class StandpointLogicProgram:
    atoms: List[str]
    standpoints: List[str]
    rules: List[SLPRule]
    goal_standpoint: str
    goal_head: str


def generate_slp(
    n_atoms: int,
    n_standpoints: int,
    n_rules_per_sp: int,
    max_pos_body: int,
    max_neg_body: int,
) -> StandpointLogicProgram:
    atoms = [f"a{i}" for i in range(1, n_atoms + 1)]
    standpoints = [f"s{i}" for i in range(1, n_standpoints + 1)]

    rules: List[SLPRule] = []
    for sp in standpoints:
        for _ in range(n_rules_per_sp):
            head = random.choice(atoms)
            rest = [a for a in atoms if a != head]
            k_pos = random.randint(0, max_pos_body)
            pos_body = random.sample(rest, min(k_pos, len(rest)))
            remaining = [a for a in rest if a not in pos_body]
            k_neg = random.randint(0, max_neg_body)
            neg_body = random.sample(remaining, min(k_neg, len(remaining)))
            rules.append(SLPRule(standpoint=sp, head=head, pos_body=pos_body, neg_body=neg_body))

    goal_rule = rules[-1]
    return StandpointLogicProgram(
        atoms=atoms,
        standpoints=standpoints,
        rules=rules,
        goal_standpoint=goal_rule.standpoint,
        goal_head=goal_rule.head,
    )


def _nested_and(terms: List[str]) -> str:
    if not terms:
        raise ValueError("Cannot create and from empty list")
    if len(terms) == 1:
        return terms[0]
    result = terms[-1]
    for term in reversed(terms[:-1]):
        result = f"and({term},{result})"
    return result


# ABA framework F(P), per Definition 7.2:
#   A := {(~p_{m+i})^s}, contrary((~p)^s) := p^s
#   R := {p0^s <- p1^s,...,pm^s,(~pm+1)^s,...,(~pm+n)^s}
def slp_to_aba(P: StandpointLogicProgram) -> str:
    assumptions: List[str] = []
    contraries: List[Tuple[str, str]] = []
    seen_assumptions: Set[str] = set()
    rule_lines: List[str] = []

    rule_id = 1
    for r in P.rules:
        S = r.standpoint
        head_atom = f"{r.head}_{S}"
        body_atoms = [f"{p}_{S}" for p in r.pos_body]

        for p in r.neg_body:
            asm_atom = f"not_{p}_{S}"
            contrary_atom = f"{p}_{S}"
            if asm_atom not in seen_assumptions:
                seen_assumptions.add(asm_atom)
                assumptions.append(asm_atom)
                contraries.append((asm_atom, contrary_atom))
            body_atoms.append(asm_atom)

        if body_atoms:
            rule_lines.append(f"% {head_atom} <- {', '.join(body_atoms)}")
        else:
            rule_lines.append(f"% {head_atom}.")
        rule_lines.append(f"head({rule_id},{head_atom}).")
        for b in body_atoms:
            rule_lines.append(f"body({rule_id},{b}).")
        rule_lines.append("")
        rule_id += 1

    lines: List[str] = []
    if assumptions:
        lines.append("assumption(" + ";".join(assumptions) + ").")
        lines.append("")
        for asm_atom, contrary_atom in contraries:
            lines.append(f"contrary({asm_atom},{contrary_atom}).")
        lines.append("")
    lines.extend(rule_lines)
    lines.append("% goal")
    lines.append(f"g({P.goal_head}_{P.goal_standpoint}).")

    return "\n".join(lines)


# NM-S4FSL ASP encoding, per Definition 7.1:
#   []s(p0) <- []s(p1) ^ ... ^ []s(pm) ^ []s¬[]s(pm+1) ^ ... ^ []s¬[]s(pm+n)
def slp_to_s4fs_asp(P: StandpointLogicProgram) -> str:
    lines: List[str] = []
    if len(P.atoms) > 1:
        lines.append("% Atom ordering")
        for a, b in zip(P.atoms, P.atoms[1:]):
            lines.append(f"succ({a},{b}).")
        lines.append("")

    for r in P.rules:
        S = r.standpoint
        if not r.pos_body and not r.neg_body:
            lines.append(f"%{S}: {r.head}")
            lines.append(f"form(box({S},{r.head})).")
            continue

        body_terms = [f"box({S},{p})" for p in r.pos_body]
        body_terms += [f"box({S},neg(box({S},neg({p}))))" for p in r.neg_body]
        body = _nested_and(body_terms)
        formula = f"neg(and({body},neg(box({S},{r.head}))))"

        body_strs = r.pos_body + [f"~{p}" for p in r.neg_body]
        lines.append(f"%{S}: {r.head} <- {', '.join(body_strs)}")
        lines.append(f"form({formula}).")

    lines.append("% goal")
    lines.append(f":- not known(box({P.goal_standpoint},{P.goal_head})).")

    return "\n".join(lines)


def _clear_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)
    for name in os.listdir(path):
        full = os.path.join(path, name)
        if os.path.isfile(full) or os.path.islink(full):
            os.remove(full)
        elif os.path.isdir(full):
            shutil.rmtree(full)


if __name__ == "__main__":
    N_PROGRAMS_PER_CONFIG = 3

    configs = [
        # (n_atoms, n_standpoints, n_rules_per_standpoint, max_body),
        (8, 1, 2, 2),
        (12, 2, 3, 2),
        (16, 3, 4, 2),
        (20, 4, 5, 2),
    ]

    _clear_dir(OUTPUT_INSTANCES_MSDIS)
    _clear_dir(OUTPUT_INSTANCES_NMSL)

    rows = [["instance", "goal", "standpoint"]]

    for i, (n_atoms, n_sp, n_rules_per_sp, max_body) in enumerate(configs, start=1):
        for j in range(1, N_PROGRAMS_PER_CONFIG + 1):
            P = generate_slp(
                n_atoms=n_atoms,
                n_standpoints=n_sp,
                n_rules_per_sp=n_rules_per_sp,
                max_pos_body=max_body,
                max_neg_body=max_body,
            )

            instance_name = f"instance_{i}_{j}.lp"

            with open(os.path.join(OUTPUT_INSTANCES_MSDIS, instance_name), "w") as f:
                f.write(slp_to_aba(P))

            with open(os.path.join(OUTPUT_INSTANCES_NMSL, instance_name), "w") as f:
                f.write(slp_to_s4fs_asp(P))

            rows.append([instance_name, P.goal_head, P.goal_standpoint])

    with open(OUTPUT_METADATA, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)
