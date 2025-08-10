import os
import re

LEVELS_BASIC = ["Level_0", "level 1", "Level_2", "Level_3", "Level_4", "Level_5", "Level_6", "Level_7", "Level_8", "Level_9", "Level_10"]
LEVELS_INTERMEDIATE = ["Level_0", "Level_1", "Level_2", "Level_3", "Level_4", "Level_5"]
LEVELS_ADVANCE = ["leve_0", "leve_1", "leve_2", "leve_3", "leve_4", "leve_5"]

MIN_SOLUTIONS = 60
BASE_PATH = "."
README_FILE = "README.md"

def count_c_files(path):
    if not os.path.exists(path):
        return 0, []
    files = os.listdir(path)
    c_files = [f for f in files if f.endswith(".c")]
    return len(c_files), c_files

def make_progress_line(level_name, count, minimum):
    status = "✅" if count >= minimum else "❌"
    return f"- **{level_name}** ({status} {count} / {minimum})"

def generate_section(name, levels, folder):
    lines = [f"## 📁 {name}"]
    total_q = len(levels) * MIN_SOLUTIONS
    total_s = 0
    for lvl in levels:
        path = os.path.join(BASE_PATH, folder, lvl)
        count, cfiles = count_c_files(path)
        total_s += count
        lines.append(make_progress_line(lvl, count, MIN_SOLUTIONS))
        if count > 0:
            for f in cfiles:
                link = os.path.join(folder, lvl, f).replace("\\", "/")
                lines.append(f"  - [{f}]({link})")
        else:
            lines.append("  - *(No solutions yet)*")
    lines.append("")
    return lines, total_q, total_s

def update_readme():
    if not os.path.exists(README_FILE):
        print("README.md not found!")
        return

    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(r"<!-- AUTO-START -->(.*?)<!-- AUTO-END -->", re.DOTALL)

    basic_sec, basic_total, basic_solved = generate_section("Basic-Prog", LEVELS_BASIC, "Basic-Prog")
    inter_sec, inter_total, inter_solved = generate_section("Intermediate", LEVELS_INTERMEDIATE, "Intermediate")
    adv_sec, adv_total, adv_solved = generate_section("Advance", LEVELS_ADVANCE, "Advance")

    total_questions = basic_total + inter_total + adv_total
    total_solutions = basic_solved + inter_solved + adv_solved
    total_pending = total_questions - total_solutions

    progress_table = [
        "## 📊 Progress Summary",
        "",
        "| Category     | Levels | Total Questions | Solutions Added | Pending |",
        "|--------------|--------|-----------------|-----------------|---------|",
        f"| Basic        | {len(LEVELS_BASIC)}      | {basic_total}           | {basic_solved}               | {basic_total - basic_solved}     |",
        f"| Intermediate | {len(LEVELS_INTERMEDIATE)}      | {inter_total}           | {inter_solved}               | {inter_total - inter_solved}     |",
        f"| Advance      | {len(LEVELS_ADVANCE)}      | {adv_total}           | {adv_solved}               | {adv_total - adv_solved}     |",
        f"| **Total**    | {len(LEVELS_BASIC) + len(LEVELS_INTERMEDIATE) + len(LEVELS_ADVANCE)}     | {total_questions}          | {total_solutions}              | {total_pending}    |",
        ""
    ]

    auto_content = (
        "<!-- AUTO-START -->\n"
        + "\n".join(basic_sec)
        + "\n"
        + "\n".join(inter_sec)
        + "\n"
        + "\n".join(adv_sec)
        + "\n"
        + "\n".join(progress_table)
        + "<!-- AUTO-END -->"
    )

    if pattern.search(content):
        new_content = pattern.sub(auto_content, content)
    else:
        new_content = content.strip() + "\n\n" + auto_content

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("README.md updated!")

if __name__ == "__main__":
    update_readme()
