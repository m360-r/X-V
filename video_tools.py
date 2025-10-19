import base64
import os

VIDEO_PATH = "video.mp4"       # ইনপুট ভিডিও ফাইল
COPY_PATH = "copy.mp4"         # কপি করা ফাইল
EMBED_HTML = "video_embed.html"  # Base64 সহ HTML ফাইল

# Step 1: ভিডিও ফাইল কপি করা
if os.path.exists(VIDEO_PATH):
    with open(VIDEO_PATH, "rb") as src:
        data = src.read()

    with open(COPY_PATH, "wb") as dst:
        dst.write(data)

    print(f"✅ ভিডিও কপি তৈরি হয়েছে: {COPY_PATH}")
else:
    print("❌ ভিডিও ফাইল পাওয়া যায়নি!")

# Step 2: Base64 করে HTML ফাইল বানানো (ছোট ভিডিওর জন্য)
if len(data) < 5 * 1024 * 1024:  # 5MB সীমা
    b64 = base64.b64encode(data).decode("ascii")
    html = f"""
    <!doctype html>
    <html>
      <body>
        <h2>Base64 Embedded Video</h2>
        <video controls width="480" src="data:video/mp4;base64,{b64}"></video>
      </body>
    </html>
    """
    with open(EMBED_HTML, "w", encoding="utf-8") as h:
        h.write(html)
    print(f"✅ HTML তৈরি হয়েছে: {EMBED_HTML}")
else:
    print("⚠️ ভিডিও অনেক বড় — Base64 embed করা হয়নি (৫MB-এর বেশি)")
