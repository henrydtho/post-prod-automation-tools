import os
import subprocess
import csv
from datetime import datetime

input_dir = "sample_input"
output_dir = "output"
log_file = "transcode_log.csv"

os.makedirs(output_dir, exist_ok=True)

video_extensions = [".mov", ".mxf", ".mp4", ".avi"]

with open(log_file, mode="w", newline="") as logfile:
    log_writer = csv.writer(logfile)
    log_writer.writerow(["Filename", "Status", "Timestamp"])

    for filename in os.listdir(input_dir):
        name, ext = os.path.splitext(filename)
        if ext.lower() not in video_extensions:
            continue

        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, f"{name}_proxy.mp4")

        ffmpeg_cmd = [
            "ffmpeg", "-i", input_path,
            "-c:v", "libx264", "-preset", "fast", "-crf", "23",
            "-c:a", "aac", "-b:a", "128k",
            "-y", output_path
        ]

        try:
            subprocess.run(ffmpeg_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            log_writer.writerow([filename, "Success", datetime.now()])
            print(f"[OK] {filename}")
        except subprocess.CalledProcessError:
            log_writer.writerow([filename, "Failed", datetime.now()])
            print(f"[FAIL] {filename}")
