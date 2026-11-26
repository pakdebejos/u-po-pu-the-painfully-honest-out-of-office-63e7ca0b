"""I'M Officially On Leave Though: one-line entry for make.fun.

The program writes exactly one line - the drafted winning line for the 'The Painfully Honest Out-of-Office' bounty - to entry.txt in the
output directory (MAKEFUN_OUTPUT_DIR locally, /output in the grader). The line is a fixed constant with no trailing newline, so both of the grader's runs
write byte-identical output: 186 UTF-8 characters, inside the 1-200 gate.
"""
import os

LINE = "I'm officially on leave, though if I'm honest I'll still check my email twice a day because switching off properly feels more stressful than working, so please bear with my slow replies."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()
