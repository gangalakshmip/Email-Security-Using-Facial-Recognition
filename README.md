# 🔐 Email Security using Facial Recognition 📧  

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  
![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=opencv&logoColor=white)  
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)  
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)  
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)  

---

## 🌟 Overview  
Traditional password-based logins are vulnerable to phishing, brute-force, and credential leaks.  
This project adds an extra layer of protection by integrating **Facial Recognition** into the email login process — accessible via **Command Prompt only**.  

---

## ⚙️ Tech Stack  
- 🐍 **Python**, NumPy  
- 👁️ **OpenCV** (Haar cascades + CNN models)  
- 🤖 **TensorFlow/Keras** (Face recognition training)  

---

## 🔑 Authentication Flow  
1️⃣ Enter email credentials  
2️⃣ Webcam activates for real-time face capture  
3️⃣ Compare face with registered dataset  
✅ **Match → Access granted**  
❌ **No match → Access denied**  

---

## 🔒 Security Features  
- Two-factor authentication (**Password + Face**)  
- Live detection to prevent replay attacks 🎭  
- Failed attempts logged for monitoring 📜  

---

## 🚀 Run the Project  
```bash
git clone https://github.com/yourusername/email-facial-recognition.git
cd email-facial-recognition
pip install -r requirements.txt
python main.py
