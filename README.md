# 🔐 Password Hashing & Brute-force Simulation

This Python mini-project demonstrates how passwords are securely hashed using `bcrypt`, and how a dictionary-based brute-force attack can attempt to crack those hashes. Great for cybersecurity students exploring password security concepts.

## ⚙️ Features

- Securely hashes passwords with `bcrypt`
- Validates password inputs
- Simulates a brute-force attack using a sample wordlist
- CLI support for easy testing

## 📁 Project Files

- `password_security_sim.py` – main script
- `wordlist.txt` – basic dictionary for brute-force simulation

## 🐍 Requirements

- Python 3.7+
- `bcrypt` library

## 🔧 Setup

```bash
git clone https://github.com/your-username/password-security-sim.git
cd password-security-sim

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate

# Install bcrypt
pip install bcrypt
