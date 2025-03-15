# 🔥 **MultiTool - Advanced OSINT & Cybersecurity Toolkit**  

MultiTool is an advanced **OSINT (Open Source Intelligence)** and **Cybersecurity** tool designed for penetration testers, security researchers, and ethical hackers.  

### **Features:**  
✅ **IP & Domain Recon** (WHOIS, GeoIP, Reverse DNS)  
✅ **Port Scanning** (Full Nmap-based scanning)  
✅ **Web Security Scans** (SSL, HTTP Headers, CMS detection)  
✅ **Data Breach Checks** (Have I Been Pwned API)  
✅ **OSINT Tools** (Shodan, VirusTotal, ASN lookup)  
✅ **Dark Web Search** (Find leaked credentials)  
✅ **Fast Multi-threaded Scanning**  
✅ **CLI-based & easy to use**  

---

### 👑 **Developed By:**  
🔹 **@ttvwetboi** — Ethical hacker & OSINT specialist.  
🔹 **@loxtvfx.** (Discord) — Learning & leveling up in cybersecurity.  

💀 **Built for hackers, by hackers.** Stay anonymous. Stay ahead.  

---

# ⚡ **Installation & Setup**  

## ✅ **Step 1: Install Python**  
### **Check if Python is installed**  
Run this command in PowerShell or Command Prompt:  
```powershell
python --version
```
If Python is installed, you'll see an output like this:  
```
Python 3.10.4
```
If not, download and install **Python 3.10+** from:  
👉 **[https://www.python.org/downloads/](https://www.python.org/downloads/)**  

### **After installing Python:**  
1. **Check if pip is installed:**  
   ```powershell
   python -m ensurepip --default-pip
   ```
2. **Upgrade pip:**  
   ```powershell
   python -m pip install --upgrade pip
   ```

---

## ✅ **Step 2: Clone the Repository**  
In PowerShell or Command Prompt, run:  
```powershell
git clone https://github.com/SheLovesLqwid/MultiTool---Advanced-OSINT-Cybersecurity-Toolkit
cd python-multitool
```
💡 If you don’t have Git installed, download it here:  
👉 **[https://git-scm.com/downloads](https://git-scm.com/downloads)**  

---

## ✅ **Step 3: Install Required Packages**  
Run:  
```powershell
pip install -r requirements.txt
```
If you get an error, try:  
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## ✅ **Step 4: Set Up API Keys**  
This tool requires API keys for full functionality. Follow the steps below to get your API keys.

### 🔍 **How to Get API Keys**  

### **1️⃣ Shodan API Key** (For OSINT & Network Intelligence)  
🔗 **Sign up for Shodan:** [https://account.shodan.io/register](https://account.shodan.io/register)  

📌 **Steps to Get the Key:**  
1. **Create an account** on Shodan.  
2. **Log in** and go to **[My Account](https://account.shodan.io/)**.  
3. **Copy your API key** from the "API Key" section.  

💡 **Free accounts** get **basic searches**, but for advanced features, a paid account is required.

---

### **2️⃣ Have I Been Pwned (HIBP) API Key** (For Checking Data Breaches)  
🔗 **Get the API key here:** [https://haveibeenpwned.com/API/Key](https://haveibeenpwned.com/API/Key)  

📌 **Steps to Get the Key:**  
1. **Go to the API page** and sign up.  
2. **Purchase an API key** (costs about **$3.50/month**).  
3. **Copy the key** after purchase.  

💡 This is required to check **if an email has been part of a data breach**.

---

### **3️⃣ VirusTotal API Key** (For Malware & URL Scanning)  
🔗 **Get the API key here:** [https://www.virustotal.com/gui/join-us](https://www.virustotal.com/gui/join-us)  

📌 **Steps to Get the Key:**  
1. **Sign up** for a free account on VirusTotal.  
2. **Log in** and go to **[Your API Keys](https://www.virustotal.com/gui/my-apikey)**.  
3. **Copy your API key** from the dashboard.  

💡 **Free API keys** have a request limit, while **paid keys** offer more scans.

---

### **4️⃣ Hunter.io API Key** (For Email OSINT & Domain Search)  
🔗 **Get the API key here:** [https://hunter.io/api-keys](https://hunter.io/api-keys)  

📌 **Steps to Get the Key:**  
1. **Create an account** on Hunter.io.  
2. **Log in** and go to **API Keys**.  
3. **Copy your API key** from the dashboard.  

💡 This helps find **email addresses related to a domain**.

---

## ✅ **Step 5: Add API Keys to `config.json`**  
Once you have all the API keys, edit `config.json` and replace `"YOUR_API_KEY"` with your actual keys:

```json
{
    "shodan_api": "YOUR_REAL_SHODAN_API_KEY",
    "hibp_api": "YOUR_REAL_HIBP_API_KEY",
    "virustotal_api": "YOUR_REAL_VIRUSTOTAL_API_KEY",
    "hunter_api": "YOUR_REAL_HUNTER_API_KEY"
}
```

---

# 🚀 **How to Use MultiTool**  

Run the tool:  
```powershell
python multitool.py --help
```
This will show all available commands.

---

### 🔍 **1. Perform a WHOIS Lookup**  
```powershell
python multitool.py whois google.com
```

---

### 🔥 **2. Scan an IP for Open Ports**  
```powershell
python multitool.py scan-ip 192.168.1.1 --ports 1-65535
```

---

### 🛡 **3. Run a Full Web Security Scan**  
```powershell
python multitool.py webscan example.com
```

---

### 📧 **4. Check if an Email Has Been Leaked in a Data Breach**  
```powershell
python multitool.py breach-check test@example.com
```

---

### 🕵️‍♂️ **5. Shodan OSINT Lookup**  
```powershell
python multitool.py shodan "port:22 country:US"
```

---

### 🌍 **6. Dark Web Search**  
```powershell
python multitool.py darkweb bitcoin
```

---

### 📜 **7. Generate a Security Report (JSON, Markdown, HTML)**  
```powershell
python multitool.py report json
```

---

# 🛠 **Troubleshooting**  

### ❌ **pip install -r requirements.txt Fails**  
Try running:  
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

### ❌ **Invalid Command!**  
Make sure you're using the correct format. Run:  
```powershell
python multitool.py --help
```
to see available commands.

---

### ❌ **Shodan / HIBP API Not Working**  
Ensure your API key is correctly added to `config.json`. Also, verify that your API subscription is active.

---

# 🤝 **Join Our Discord Community!**  
Need help or want to contribute? Join our **Discord server**:  
👉 **[https://discord.gg/4W9a9ynbuP](https://discord.gg/4W9a9ynbuP)**  

---

# 🌟 **Contributing**  
Want to improve MultiTool? Submit **Pull Requests** or suggest features!  

```powershell
git checkout -b feature-branch
git commit -m "Added a new feature"
git push origin feature-branch
```

---

# 📜 **License**  
This project is licensed under the **MIT License**.  
