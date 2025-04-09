# 🎧 Moodify – AI-Powered Music Recommender Based on Your Mood

Moodify is a real-time AI app that uses your **facial expression** to detect your emotion and automatically plays music that matches your vibe using the **Spotify API**.

---

## 🔥 Features

- 🎭 Real-time **emotion detection** via webcam
- 🎶 Personalized **Spotify playlist** selection
- ⚡ Simple to run, fun to use
- 🤖 Powered by DeepFace, OpenCV, and Spotipy

---

## 🧠 Tech Stack

- Python
- OpenCV
- DeepFace
- Spotipy

---

## 🚀 How to Run

1. Clone the repo
```bash
git clone https://github.com/yourusername/Moodify.git
cd Moodify
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Set up your Spotify Developer credentials at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard), and paste them in `moodify.py`:
```python
SPOTIFY_CLIENT_ID = "your_client_id"
SPOTIFY_CLIENT_SECRET = "your_client_secret"
SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback"
```

4. Run the app
```bash
python moodify.py
```

---

## 🎬 Demo

*(Add a GIF here if you want to show off the magic)*

---

## 🛠️ Future Upgrades

- Streamlit Web UI
- Mood logs/history
- Voice command support
- Mobile app integration

---

## 🙌 Credits

- [DeepFace](https://github.com/serengil/deepface)
- [OpenCV](https://opencv.org/)
- [Spotipy](https://spotipy.readthedocs.io/)

---

## ✨ License

MIT – free to vibe and remix.
