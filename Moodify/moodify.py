# 🎧 Moodify – Facial Emotion to Spotify Playlist Recommender

import cv2
from deepface import DeepFace
import time
from spotipy.oauth2 import SpotifyOAuth
import spotipy

# ---------------------- CONFIG ----------------------
SPOTIFY_CLIENT_ID = "YOUR_CLIENT_ID"
SPOTIFY_CLIENT_SECRET = "YOUR_CLIENT_SECRET"
SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback"

EMOTION_TO_PLAYLIST = {
    "happy": "spotify:playlist:37i9dQZF1DXdPec7aLTmlC",
    "sad": "spotify:playlist:37i9dQZF1DWVrtsSlLKzro",
    "angry": "spotify:playlist:37i9dQZF1DWZHwH4ZxjqpS",
    "neutral": "spotify:playlist:37i9dQZF1DWZeKCadgRdKQ",
    "surprise": "spotify:playlist:37i9dQZF1DX2pSTOxoPbx9",
    "fear": "spotify:playlist:37i9dQZF1DWZ0wrsBX3TBu",
    "disgust": "spotify:playlist:37i9dQZF1DWU0ScTcjJBdj"
}

# ---------------------- SPOTIFY AUTH ----------------------
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-read-playback-state,user-modify-playback-state"
))

def play_playlist(emotion):
    uri = EMOTION_TO_PLAYLIST.get(emotion, EMOTION_TO_PLAYLIST["neutral"])
    print(f"\n🎵 Playing playlist for emotion: {emotion} -> {uri}")
    sp.start_playback(context_uri=uri)

# ---------------------- EMOTION DETECTION ----------------------
cap = cv2.VideoCapture(0)
last_emotion = ""
last_time = time.time()
interval = 10  # seconds between updates

print("\n🔍 Moodify is detecting your mood... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']

        if emotion != last_emotion and time.time() - last_time > interval:
            play_playlist(emotion)
            last_emotion = emotion
            last_time = time.time()

        cv2.putText(frame, f"Emotion: {emotion}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    except Exception:
        cv2.putText(frame, "No face detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Moodify Cam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
