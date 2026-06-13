import re
import numpy as np
from pathlib import Path


def split_records(text):
    """
    Splits a text file into complete top-level list records.
    This handles cases where one record spans multiple physical lines.
    """
    records = []
    buffer = []
    depth = 0

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue

        depth += stripped.count("[")
        depth -= stripped.count("]")

        buffer.append(stripped)

        if depth == 0 and buffer:
            records.append(" ".join(buffer))
            buffer = []

    if buffer:
        raise ValueError("Unclosed bracket structure found in input file.")

    return records


def parse_input_record(record):
    """
    Parses one combined input record containing 8 array([...]) entries.
    """
    matches = re.findall(r"array\(\[(.*?)\]\)", record, flags=re.DOTALL)

    if len(matches) != 8:
        raise ValueError(f"Expected 8 input arrays, found {len(matches)}")

    parsed = []
    for m in matches:
        cleaned = m.replace("\n", " ")
        values = [float(x) for x in re.split(r"[,\s]+", cleaned.strip()) if x]
        parsed.append(np.array(values, dtype=float))

    return parsed


def parse_output_record(record):
    """
    Parses one combined output record containing 8 np.float64(...) values.
    """
    matches = re.findall(r"np\.float64\((.*?)\)", record)

    if len(matches) != 8:
        raise ValueError(f"Expected 8 output values, found {len(matches)}")

    return [float(x) for x in matches]


def append_week(week_id, inputs_txt, outputs_txt, repo_root):
    """
    Reads combined weekly university input/output txt files,
    splits them into 8 functions, appends to observed data,
    and stores per-function weekly update files.
    """

    repo_root = Path(repo_root)

    inputs_txt = repo_root / inputs_txt
    outputs_txt = repo_root / outputs_txt

    input_text = inputs_txt.read_text()
    output_text = outputs_txt.read_text()

    input_records = split_records(input_text)
    output_records = split_records(output_text)

    print(f"Detected input records: {len(input_records)}")
    print(f"Detected output records: {len(output_records)}")

    if len(input_records) != len(output_records):
        raise ValueError(
            f"Mismatch in records: inputs={len(input_records)}, outputs={len(output_records)}"
        )

    for row_idx, (input_record, output_record) in enumerate(zip(input_records, output_records), start=1):

        inputs_all = parse_input_record(input_record)
        outputs_all = parse_output_record(output_record)

        for f_id in range(1, 9):

            f_path = repo_root / f"data/processed/function_{f_id}"

            x_new = inputs_all[f_id - 1]
            y_new = outputs_all[f_id - 1]

            obs_x_path = f_path / "observed_inputs.npy"
            obs_y_path = f_path / "observed_outputs.npy"

            X_old = np.load(obs_x_path)
            y_old = np.load(obs_y_path)

            X_updated = np.vstack([X_old, x_new.reshape(1, -1)])
            y_updated = np.append(y_old, y_new)

            np.save(obs_x_path, X_updated)
            np.save(obs_y_path, y_updated)

            week_dir = f_path / "weekly_updates"
            week_dir.mkdir(exist_ok=True)

            np.save(week_dir / f"{week_id}_record_{row_idx}_input.npy", x_new)
            np.save(week_dir / f"{week_id}_record_{row_idx}_output.npy", np.array([y_new]))

    print(f"✅ {week_id} successfully appended to all 8 functions")
