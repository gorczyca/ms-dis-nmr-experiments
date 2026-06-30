import sys, subprocess
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from config import CONFIG

TIMEOUT = 60
FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"

# (fixture name, expected result) per solver family
CASES = [
    ("yes", "YES"),
    ("no", "NO"),
]

if __name__ == "__main__":
    setup = sys.argv[1] if len(sys.argv) > 1 else "local"

    failures = []
    for solver in CONFIG:
        family = "aba" if solver.startswith("msdis") else "asp"
        for case_name, expected in CASES:
            instance_path = FIXTURES_DIR / f"{case_name}.{family}.lp"
            cmd = CONFIG[solver][setup].format(instance=instance_path)

            print(f"=== {solver} / {case_name} (expect {expected}, {setup}) ===")
            print(cmd)
            try:
                out = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=TIMEOUT).decode().strip()
                print(out)
                if out != expected:
                    failures.append(f"{solver}/{case_name}: expected {expected}, got {out!r}")
            except Exception as e:
                print(f"FAILED: {e}")
                failures.append(f"{solver}/{case_name}: {e}")
            print()

    if failures:
        print("SETUP CHECK FAILED:")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)

    print("SETUP CHECK OK")
