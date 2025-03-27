# 🐝 Simple Honeypot in Python

This is a **basic TCP honeypot** that listens for incoming connections and logs intrusion attempts. It simulates a service to detect unauthorized access attempts.

## 🚀 Features
- **Listens on a specified port (default: 8080).**
- **Logs intrusion attempts** to `honeypot.log`.
- **Sends a fake response** to trick attackers.

## 🛠 Installation

### 1️⃣ Install Python (if not installed)
Ensure you have Python 3 installed:
```bash
python3 --version
```

### 2️⃣ Save the script
Save the honeypot script as `honeypot.py`.

## 🏃‍♂️ Running the Honeypot
```bash
python3 honeypot.py
```
*For privileged ports (below 1024), run with sudo:*
```bash
sudo python3 honeypot.py
```

## 🔎 Testing the Honeypot
Open another terminal and try:
```bash
nc 127.0.0.1 8080
```
Expected response:
```
Access Denied! Logged.
```

## 📜 Viewing Logs
To check logged intrusions:
```bash
cat honeypot.log
```

## 🔐 Use Cases
- **Monitor suspicious activity** on a network.
- **Detect unauthorized access attempts.**
- **Deploy as a decoy to mislead attackers.**


👨‍💻 **Happy Honeypotting!** 🐝

