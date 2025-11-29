<h1 align="center">💥 Video-Spam-Prankware</h1>
<p align="center">
  <em>🎬 A small Python tool that repeatedly plays a video at random screen positions as a prank.</em>
</p>

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.x-blue.svg" />  
    <img src="https://img.shields.io/badge/Status-Experimental-orange.svg" />  
    <img src="https://img.shields.io/badge/Project-Type%3A%20Prankware-ff69b4.svg" />
</p>

---

## 🌟 Overview

This project plays a custom video with synchronized audio at random positions on the screen in a continuous loop.  
It is intended as a harmless prank program (prankware) to surprise the user by repeatedly showing the video and eventually crashing their PC.

---

## 📂 File Structure

### `run.py`
▶️ The entry point of the project.  
Repeatedly launches `main.py` according to the desired number of iterations.

### `main.py`
⚙️ Core functionality:

- 🖥️ Detects screen resolution  
- 🎯 Generates random playback coordinates  
- 🎬 Plays video and audio in sync  
- 🔝 Keeps the window in the foreground  

---

## 🛠 Installation

**1. Clone the repository:**
   
```bash
git clone https://github.com/JXR0N/Video-Spam-Prankware.git
cd Video-Spam-Prankware
```
**2. Install dependencies:**
```bash
pip install -r requirements.txt
```
**3. Run the application:**
```bash
python run.py
```
