# post-prod-automation-tools
Media workflow scripts for post production engineering tasks
# FFmpeg Transcode Automation

This Python script batch-transcodes all video files in a folder into H.264 MP4 proxies using FFmpeg. It also generates a CSV report of the results.

---

## 🔧 Features
- Supports .mov, .mxf, .mp4, and .avi files
- Uses FFmpeg with x264 encoding
- Auto-creates output directory and logs status to CSV
- Command line execution, works cross-platform

---

## ▶️ How to Use

1. Install Python 3.9+ and FFmpeg
2. Place your source files into the `sample_input` folder
3. Run:
   ```bash
   python3 transcode_to_mp4.py
4. Check `output/` for proxies and `transcode_log.csv` for results
