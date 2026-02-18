# 🎨 Sketchbot

### *Transforming Pixels into Pencil Strokes*

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/harisankarsnair/Sketchbot/main/main.py)
[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Sketchbot** is a minimalist yet powerful Computer Vision tool that uses Gaussian mathematical blending to turn any photograph into a realistic pencil sketch. 

---

## 🧠 How the Magic Happens

Behind the curtain, Sketchbot runs a 4-stage image processing pipeline:

| Stage | Process | Result |
| :--- | :--- | :--- |
| **01** | **Grayscale** | Removes color noise |
| **02** | **Inversion** | Prepares the negative mask |
| **03** | **Gaussian Blur** | Smooths out the details |
| **04** | **Color Dodge** | Divides original by blur to reveal edges |

---

## 🛠️ Tech Stack

* **Python:**
* **Streamlit:**
* **OpenCV:** 
* **NumPy:** 

---

## 🚀 Run it Locally

Want to experiment with the code?

```bash
# Clone the repo
git clone [https://github.com/harisankarsnair/Sketchbot.git](https://github.com/harisankarsnair/Sketchbot.git)

# Install dependencies
pip install -r requirements.txt

# Launch the bot
streamlit run main.py

---

## 🤝 Contributing
1. **Fork** the project.
2. Create your **Feature Branch** (`git checkout -b feature/AmazingFeature`).
3. **Commit** your Changes (`git commit -m 'Add some AmazingFeature'`).
4. **Push** to the Branch (`git push origin feature/AmazingFeature`).
5. Open a **Pull Request**.

---
*Created with ❤️ by [Harisankar S Nair](https://github.com/harisankarsnair)*
