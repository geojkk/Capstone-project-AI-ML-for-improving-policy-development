import numpy as np
import re
from pathlib import Path


# -----------------------------------------------------------
# Parse one line from inputs.txt
# -----------------------------------------------------------
def parse_input_line(line):
    matches = re.findall(r'array\(\[(.*?)\]\)', line)
    parsed = []
    for m in matches:
        arr = np.array([float(x.strip()) for x in m.split(",")])
        parsed.append(arr)
    return parsed  # list of 8 arrays


# -----------------------------------------------------------
# Parse one line from outputs.txt
# -----------------------------------------------------------
def parse_output_line(line):
    matches = re.findall(r'np.float64\((.*?)\)', line)
    return [float(x) for x in matches]  # list of 8 scalars


# -----------------------------------------------------------
# Append weekly results to each function
# -----------------------------------------------------------
def append_week(
    week_id,
    inputs_txt,
    outputs_txt,
    repo_root
):

    repo_root = Path(repo_root)

    input_lines = open(inputs_txt).read().strip().split("\n")
    output_lines = open(outputs_txt).read().strip().split("\n")

    assert len(input_lines) == len(output_lines), "Mismatch in input/output rows"

    for i in range(len(input_lines)):

        inputs_all = parse_input_line(input_lines[i])
        outputs_all = parse_output_line(output_lines[i])

        for f_id in range(1, 9):

            f_path = repo_root / f"data/function_{f_id}"

            x_new = inputs_all[f_id - 1]
            y_new = outputs_all[f_id - 1]

            # Load existing observed data
            obs_x_path = f_path / "observed_inputs.npy"
            obs_y_path = f_path / "observed_outputs.npy"

            X_old = np.load(obs_x_path)
            y_old = np.load(obs_y_path)

            # Append
            X_new = np.vstack([X_old, x_new.reshape(1, -1)])
            y_new_full = np.append(y_old, y_new)

            np.save(obs_x_path, X_new)
            np.save(obs_y_path, y_new_full)

            # Save weekly update separately
            week_dir = f_path / "weekly_updates"
            week_dir.mkdir(exist_ok=True)

            np.save(week_dir / f"{week_id}_input.npy", x_new)
            np.save(week_dir / f"{week_id}_output.npy", y_new)

    print(f"✅ Week {week_id} successfully appended to all functions")