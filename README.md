# Reddit → Telegram Video Bot

This bot automatically fetches **random video / GIF-style MP4 posts** from selected subreddits and sends them to a Telegram chat or channel at a fixed interval.

Only **real Reddit videos (MP4)** are used to ensure full Telegram compatibility.

---

## ✨ Features

* 🎥 Sends Reddit videos directly to Telegram
* 🔀 Random subreddit & random post selection
* 🕒 Configurable sending interval
* 🧠 Skips unsupported or broken media
* 🖥️ Simple Python script, no database required
* 🐞 Debug logs enabled by default

---

## 📦 Requirements

* Python **3.8+**
* Telegram Bot Token
* Telegram User ID or Channel ID

---

## 🔧 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/EmirYLMZ128/reddit-telegram-video-bot/tree/main.git
cd reddit-telegram-video-bot
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

Open the `bot.py` file and edit the following lines:

```python
TELEGRAM_TOKEN = "PUT_YOUR_BOT_TOKEN_HERE"
TELEGRAM_CHATID = "PUT_YOUR_CHAT_ID_HERE"
```

---

### 📌 Subreddit Configuration

Add the subreddits you want the bot to pull videos from:

```python
SUBREDDITS = [
    "subreddit1",
    "subreddit2",
    "subreddit3"
]
```

---

### ⏱️ Change Sending Interval

Locate this line in `bot.py`:

```python
schedule.every(10).seconds.do(send_video_or_gif)
```

Examples:

**Every 1 minute**

```python
schedule.every(60).seconds.do(send_video_or_gif)
```

**Every 5 minutes**

```python
schedule.every(300).seconds.do(send_video_or_gif)
```

**Every 1 hour**

```python
schedule.every(1).hours.do(send_video_or_gif)
```

---

## ▶️ Run the Bot

Start the bot with:

```bash
python bot.py
```

If everything is working correctly, you will see:

```text
🚀 BOT IS RUNNING IN DEBUG MODE
```

---

## ⚠️ Important Notes

* Some Reddit videos may fail due to Telegram CDN limitations — this is **normal behavior**.
* The bot will automatically skip failed videos and try the next one.
* **Never upload your real Telegram bot token to GitHub.**
* This bot uses Reddit’s public JSON feed (no API key required).

---

## 📁 Recommended Project Structure

```text
reddit-telegram-video-bot/
│
├── bot.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📄 License

This project is intended for **educational and personal use only**.
Please respect Reddit and Telegram terms of service when using this bot.

---

## ❤️ Credits

Built using:

* Reddit JSON API
* python-telegram-bot
* requests
* schedule
