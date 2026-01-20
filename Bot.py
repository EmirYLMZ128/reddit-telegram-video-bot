import random
import time
import schedule
import threading
import requests
from telegram import Bot

# =========================
# TELEGRAM CONFIGURATION
# =========================

TELEGRAM_TOKEN = "PUT_YOUR_BOT_TOKEN_HERE"      # <-- Telegram Bot Token
TELEGRAM_CHATID = "PUT_YOUR_CHAT_ID_HERE"       # <-- Telegram User ID or Channel ID


# =========================
# SUBREDDIT CONFIGURATION
# =========================

# SUBREDDIT LIST IS HERE
SUBREDDITS = [
    # "subreddit1",
    # "subreddit2",
    # "subreddit3"
]


# =========================
# HEADERS
# =========================

HEADERS = {
    "User-Agent": "telegram-reddit-video-bot"
}

bot = Bot(token=TELEGRAM_TOKEN)


def send_video_or_gif():
    print("\n--- NEW ATTEMPT ---")

    subreddit = random.choice(SUBREDDITS)
    print("Selected subreddit:", subreddit)

    url = f"https://www.reddit.com/r/{subreddit}.json?limit=50"

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        posts = response.json()["data"]["children"]
    except Exception as e:
        print("❌ ERROR FETCHING REDDIT JSON:", e)
        return

    random.shuffle(posts)

    for p in posts:
        post = p["data"]
        title = post.get("title", "")

        video_url = None

        # 🎥 REAL REDDIT VIDEOS
        if post.get("is_video"):
            video_url = post["media"]["reddit_video"]["fallback_url"]

        # 🎞️ GIF-LIKE POSTS THAT ARE ACTUALLY MP4
        elif post.get("preview"):
            try:
                video_url = post["preview"]["reddit_video_preview"]["fallback_url"]
            except:
                pass

        if not video_url:
            continue

        print("🎥 VIDEO URL FOUND:", video_url)

        try:
            bot.send_video(
                chat_id=TELEGRAM_CHATID,
                video=video_url,
                caption=title[:1024]
            )
            print("✅ VIDEO SENT SUCCESSFULLY")
            return

        except Exception as e:
            print("❌ TELEGRAM VIDEO ERROR:", e)

    print("⚠️ NO SUITABLE VIDEO FOUND THIS ROUND")


# =========================
# SCHEDULER
# =========================

# CHANGE THE INTERVAL HERE
# Example:
# every(60).seconds  -> every 1 minute
# every(300).seconds -> every 5 minutes
# every(1).hours    -> every 1 hour

schedule.every(10).seconds.do(send_video_or_gif)


def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)


print("🚀 BOT IS RUNNING IN DEBUG MODE")
threading.Thread(target=run_scheduler).start()
