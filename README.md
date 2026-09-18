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

# 🎞️ Post Production Automation Tools

Welcome! This repository contains Python and Bash tools built to automate real-world workflows in post-production environments — from transcoding to metadata extraction to delivery automation.

---

## 👨‍💻 About Me

I'm **Henry Thompson** — a post-production professional turned engineer at NBCUniversal. After a decade working with top-tier clients like Netflix, HBO, and Warner Bros., I now focus on building efficient, scalable tools that bridge editorial, operations, and technology.


---

## ⚒️ What You'll Find Here

| Tool | Description | Tech |
|------|-------------|------|
| [`ffmpeg_transcode_automation`](./ffmpeg_transcode_automation) | Batch transcodes source files to MP4 proxies and logs results | Python, FFmpeg |
| `batch_renamer` *(coming soon)* | Renames editorial dailies with structured naming | Python |
| `frameio_uploader` *(coming soon)* | Uploads and organizes assets using Frame.io API | Python, REST |
| `watchfolder_qc_trigger` *(coming soon)* | Monitors a folder and triggers QC automation on new deliveries | Bash, Shell |

---

## 🧠 Why This Repo Exists

Studios and post houses are drowning in media, metadata, and manual work. I build tools that:
- Reduce clicks and errors
- Speed up delivery and QC
- Connect creative tools with engineering systems

If you're looking for someone who can think like an editor **and** build like an engineer — we should talk.

---

## 📫 Contact

- **LinkedIn**: [linkedin.com/in/henrydthompson](https://www.linkedin.com/in/henry-thompson-26512a49/)
- **GitHub**: [github.com/henrydthompson](https://github.com/henrydtho) 
---

## 🚧 Roadmap

- [ ] Add batch file renamer
- [ ] Add Frame.io delivery script
- [ ] Add XML metadata parser
- [ ] Add IMF QC watchfolder script
