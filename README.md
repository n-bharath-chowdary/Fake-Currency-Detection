# 💵 Fake Currency Detection Using Deep Learning

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 🚀 Project Overview

This project aims to detect **fake Indian currency notes** using **deep learning** techniques. It leverages image classification models to analyze currency note features and classify them as *genuine* or *fake* in real-time.

💡 **Why?** Fake currency poses a significant threat to the economy, and manual verification is inefficient. This system brings automation, speed, and accuracy to the process.

---

## 📸 Live Demo / Interface
<table>
  <thead>
    <tr>
      <th>Input Image</th>
      <th>Model Output</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><img src="https://github.com/user-attachments/assets/d24153c6-8cf1-4104-adc2-6f0b6e5a11ff" width="300" height="200"/></td>
      <td><img src="https://github.com/user-attachments/assets/ad17ed51-a502-4c60-8c5a-f5b10bec61d8" width="300" height="200"/></td>
    </tr>
    <tr>
      <td><img src="https://github.com/user-attachments/assets/d3259137-bb0b-4d69-8005-df1d05b67e12" width="300" height="200"/></td>
      <td><img src="https://github.com/user-attachments/assets/2a77df50-ec90-4efa-9264-bcde65187859" width="300" height="200"/></td>
    </tr>
  </tbody>
</table>

## 🔍 Features

- ✅ Real-time currency image classification
- ✅ Custom-trained CNN model
- ✅ Streamlit web interface
- ✅ Cleanly structured dataset (INR denominations)
- ✅ Easily extendable for multiple currencies
- ✅ Includes model download link for easy setup

---

## 🧠 Model Download

The trained model (`fake_currency_detector.h5`) is too large for GitHub.  
👉 [Download it from Google Drive](https://drive.google.com/file/d/1Von6jY90T-obcC9jMVXW_B6p4ZTohfIL/view?usp=sharing) and place it in the project root directory.

---

## 🗂️ Dataset Structure

```bash
dataset/
├── 10/
├── 20/
├── 50/
├── 100/
├── 200/
├── 500/
├── fake/
└── background/
```
---
Each folder contains sample note images.

fake/ folder contains counterfeit currency samples.

background/ used for augmentation and background filtering.

---

## 🛠️ Installation
```
git clone https://github.com/n-bharath-chowdary/Fake-Currency-Detection.git
cd Fake-Currency-Detection
pip install -r requirements.txt
```
---
## Download the model:

[Click here to download model](https://drive.google.com/file/d/1Von6jY90T-obcC9jMVXW_B6p4ZTohfIL/view?usp=sharing)

Place fake_currency_detector.h5 in the project root folder.

---

## ▶️ How to Run

run app.py
Then, upload a currency image in the web app interface to detect if it's fake or genuine.

---

## 🧪 Algorithms Used

Convolutional Neural Networks (CNN)

Image Augmentation (OpenCV, Keras Preprocessing)

Transfer Learning (optional)

Softmax classifier for multi-class detection

---

## 📄 Project Documents
📘 Final Report: [Fake_Currency_Detection_Report.pdf](https://github.com/n-bharath-chowdary/Fake-Currency-Detection/blob/HIKE/docs/INTRODUCTION.pdf)

📊 Presentation Slides: Fake-Currency-Detection-Using-DeepLearning.ppt

📑 Research Paper: IJEDR2502037.pdf

---

## ✨ Future Enhancements
🔍 Add OCR to extract serial numbers

📱 Deploy as Android app

☁️ Integrate cloud-based verification APIs

🧾 Detect other currencies (USD, EUR, etc.)

---

## 🙋‍♂️ Author
### Bharath Chowdary

#### [GitHub](https://github.com/n-bharath-chowdary) 
#### [LinkedIn](https://www.linkedin.com/in/n-bharath-chowdary/)
