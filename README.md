# 🔐 Advanced Password Strength Checker (Flask + zxcvbn)

A secure, modern, and advanced password strength checker web app built with Python, Flask, and zxcvbn. It analyzes passwords using entropy, pattern recognition, and custom rule checks.

## 🚀 Features

* ✅ Real-time strength analysis with [zxcvbn](https://github.com/dropbox/zxcvbn)
* ✅ Custom rule checks (length, uppercase, digit, symbols, etc.)
* ✅ Entropy, crack time estimates
* ✅ Clean responsive UI
* ✅ Error handling & logging
* ✅ Future-ready architecture

## 📸 Screenshot

![App Screenshot](screenshot.png) <!-- (Add if you want later) -->

---

## 🛠️ Tech Stack

* Python 3.10+
* Flask
* zxcvbn-python
* HTML, CSS (modern styles)

---

## 🧑‍💻 How to Run Locally

### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/password-strength-checker.git
cd password-strength-checker
```

### 2. Set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate     # On Linux/macOS
venv\Scripts\activate        # On Windows
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Run the application:

```bash
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 📂 Project Structure

```
password-strength-checker/
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── app.py
├── password_strength.py
├── requirements.txt
└── README.md
```

---

## 📆 requirements.txt

```txt
Flask>=2.3.0
zxcvbn>=4.4.28
```

---

## ✅ GitHub Upload Instructions

1. Initialize your local Git repo (if not done yet):

   ```bash
   git init
   ```

2. Add files:

   ```bash
   git add .
   git commit -m "Initial commit: Advanced Password Strength Checker"
   ```

3. Create a new repo on GitHub at [https://github.com/new](https://github.com/new)

4. Link remote:

   ```bash
   git remote add origin https://github.com/yourusername/password-strength-checker.git
   git branch -M main
   git push -u origin main
   ```

---

## 🌟 Future Features (Ideas)

* Dark mode
* Password strength meter bar
* API version for integration
* User signup/login with secure password policies

---

## 📄 License

MIT License — free to use and modify.
