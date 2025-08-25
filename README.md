# Face Detection using OpenCV (Haar/DNN) — Colab Ready

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Techro0/face-detection-using-haar/blob/main/Face_Detection_using_haar.ipynb)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/opencv-4.x-informational)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

This repo provides a **human face detection** pipeline built with **OpenCV** and designed for **Google Colab**.

- **Detectors**: choose **Haar cascade** (fast, classic) or **DNN (Res10 SSD)** (more robust).
- **Datasets**: upload a **ZIP** or **TGZ/TAR** archive; the notebook extracts, runs detection on every image, and saves:
  - Annotated images → `outputs/`
  - Optional face crops → `crops/`

> ⚠️ Use responsibly. Respect privacy and obtain consent. Check local laws before using face tech.

---

## Files
- `Face_Detection_using_haar.ipynb` — Colab notebook (face detection only).
- `face_detection_using_haar.py` — Python script version (batch processing).
- `requirements.txt` — dependencies.
- `LICENSE` — MIT.
- `.gitignore` — clean repo defaults.

If you pick a different repo name than `face-detection-using-haar`, update the **Colab badge** URL at the top of this README.

---

## Quick Start (Colab)
1. Open the notebook via the **Colab badge** above (or upload the `.ipynb` to Colab).
2. Run the **Install dependencies** cell.
3. (Optional) Run the **DNN model download** cell if you plan to use the DNN detector.
4. In **Choose detector & parameters**, set:
   - `DETECTOR = "haar"` or `"dnn"`
   - Tune `scaleFactor`, `minNeighbors` (Haar) or `conf_threshold` (DNN)
5. Run **Upload dataset archive** and select your `.zip` or `.tgz/.tar` (any folder layout).
6. Run **Run face detection on dataset**.
7. (Optional) Preview random results and **zip outputs** for download.

---

## Local Use (optional)
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Batch process using the script (expects an archive in the CWD and writes outputs/ + crops/)
python face_detection_using_haar.py
```

---

## Requirements
See `requirements.txt`. Minimal set:
- opencv-python
- imutils
- matplotlib

---

## License
MIT © 2025 Techro0

---

## How to publish on GitHub (quick)
**Web UI:** Create a repo → “Add file → Upload files” → drag these files → Commit.  
**Git CLI:**
```bash
git init
git checkout -b main
git add .
git commit -m "Init: face detection (Haar/DNN) Colab-ready"
git remote add origin https://github.com/Techro0/face-detection-using-haar.git
git push -u origin main
```
