# 📦 PackOpt Competition Repository for Students

This repository contains all data and scripts for the **PackOpt Supply Chain Optimization Challenge**. 

Read about the challenge [here](https://docs.google.com/document/d/1606QUnIhZb2mcfHLsYnpekRMgBk8bFReKyUE58neie4/edit?usp=sharing).  

Sign up competition team information here [8:00 - 10:30am session](https://docs.google.com/spreadsheets/d/1TfOECLzeFd8asn13rkZQFWA20jM5qluZfvzmyl_gX4c/edit?usp=sharing) or [10:45 - 1:15pm session](https://docs.google.com/spreadsheets/d/1O72MAWO0IQMS9XzJa_fjbwqEGSaq8Mg_Mp4I_NmXOWk/edit?usp=sharing).

Check the leader board [here](https://ytyimin.github.io/packopt/).

---

## 🗂️ Repository Structure

### **Main Files and Folders**
| Folder | Description |
|--------|--------------|
| `datasets/` | Training data (years 2022–2024) for all 10 datasets. |
| `submissions/` | Folder containing participants' submissions. Each subfolder represents one team's submission. |
| `submissions/sample_submission/` | Example folder showing expected file formats for submissions. |

---

### **Key Scripts**
| Script | Purpose |
|--------|----------|
| `check_constraints.py` | Validates that a participant’s box files satisfy all dataset constraints. |
| `scoring.py` | Calculates the score for a single submission using the given inputs, demand, and constraints. |
| `evaluate.py`| 	Runs scoring across all 10 datasets for one submission. |

---

### **Supporting Files**
| File | Description |
|------|--------------|
| `requirements.txt` | Lists all Python dependencies for the environment. |
| `.gitignore` | Ensures large or sensitive files are not committed to Git. |
| `README.md` | You are here! Overview of repository structure and purpose. |

---
