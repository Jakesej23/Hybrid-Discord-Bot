# 🤖 Hybrid Discord Bot

A lightweight **hybrid Discord bot** built with `discord.py` that supports both **prefix commands (! / ?)** and **slash commands (/)**.  
The bot focuses on **simple utility tools and fun interactions**, making it easy to use and expand.

---

## ✨ Features

- ⚡ Hybrid command support (prefix + slash)
- 🎲 Random utilities (rand, roll)
- 🪙 Fun commands (coin flip, say)
- 🏓 Ping/latency checker
- 🧠 Simple and clean command structure
- 🔧 Easy to customize and extend

---

## 📜 Commands

### 🔹 Prefix Commands
You can use either `!` or `?`

- `!ping` / `?ping` → Check bot latency  
- `!coin` / `?coin` → Flip a coin  
- `!rand` / `?rand` → Generate a random number  
- `!roll` / `?roll` → Roll a dice  
- `!say <text>` / `?say <text>` → Bot repeats your message  

---

### 🔹 Slash Commands
- `/ping` → Check bot latency  
- `/coin` → Flip a coin  
- `/rand` → Generate a random number  
- `/roll` → Roll a dice  
- `/say <text>` → Bot repeats your message  

---

## 📦 Installation

### 1. Clone the repository
`bash
git clone https://github.com/Jakesej23/Hybrid-Discord-Bot.git
cd Hybrid-Discord-Bot`


2. Install dependencies

`pip install -r requirements.txt`

3. Add your bot token

Open bot.py and replace:

TOKEN = "YOUR_BOT_TOKEN_HERE"

4. Run the bot **You don’t use a discord bot hosting website for this:**

`python bot.py`


5. Run the bot **You use a discord bot hosting website for this:**

🟦 Wispbyte (very popular)

* ✔️ Free 24/7 hosting
* ✔️ Upload via dashboard / GitHub
* ✔️ Node.js + Python + more languages support
* ✔️ No “premium requirements” for basic use
* ✔️ You don’t use:

ADDITIONAL PY MODULES: Install additional python packages. Use spaces to separate.

* ✔️ But you MUST use requirements.txt only if you edit the startup – it’s not needed otherwise

👉 Advantage: super easy for beginners

👉 Disadvantage: free plan has limits

👉 No renewals: free uptime 24/7, no renewals at all 

⸻

🟩 KataBump (classic)

* ✔️ Free plan for bots
* ✔️ Web upload + SFTP
* ✔️ 24/7 hosting **with renewal every 4 days**
* ✔️ Python & Node.js support

👉 Advantage: stable and made specifically for Discord bots

👉 Disadvantage: you must renew your server every 4 days, not just once, but every 4 days

✔️ You MUST use this:

ADDITIONAL PY MODULES

Install additional python packages.
Use spaces to separate:

`discord.py python-dotenv aiohttp requests`

6. 📦 Requirements

requirements.txt:

`discord.py>=2.3.0,<3.0.0`

7. ⚙️ Tech Stack

* Python 3.10+
* discord.py (2.x)
* Discord API (Slash + Prefix commands)
