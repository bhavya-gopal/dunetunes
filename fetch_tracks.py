import spotipy
from spotipy.oauth2 import SpotifyOAuth
import serial  
from dotenv import load_dotenv
import os

load_dotenv()
alarm_playing = False

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
DEVICE_ID = os.getenv("SPOTIFY_DEVICE_ID")


# 🎵 Joe Jackson's "Night and Day" Album Track URIs
NIGHT_SIDE_TRACKS = [
    "spotify:track:15XUmdLQ9i6mHrHTpNCO70",  # Another World 
    "spotify:track:52U6BN5ztDZnWtDTCgbU9H",  # Chinatown
    "spotify:track:6945EDagXhUxOoxbwvhlqB",  # T.V. Age
    "spotify:track:4DfB6GGqNjYK8xQlA51Y9J"   # Target
]

DAY_SIDE_TRACKS = [
    "spotify:track:0tFxEmLAHasUZtTKTGV1af",  # Breaking Us in Two
    "spotify:track:5nP2PxQOXJ92OPruejH9Vt",  # Cancer
    "spotify:track:5ImoRAws2ni1qYWrLR7sqi",  # Real Men
    "spotify:track:70vRVhygf1hbTcavKMesph"   # A Slow Song
]

HEAT_WARNING_TRACK = ["spotify:track:67euHrPxIzKpzpSRLeIKhU"]


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-modify-playback-state user-read-playback-state"
))

# Serial Communication with Clue Board
serial_port = "/dev/tty.usbmodem1101"  
ser = serial.Serial(serial_port, 115200, timeout=1)

def play_tracks(tracks):
    """Plays tracks from Spotify connected device"""
    try:
        sp.start_playback(device_id=DEVICE_ID, uris=tracks)
        print(f"✅ Now Playing: {tracks}")
    except Exception as e:
        print(f"Error playing tracks: {e}")

# Read Clue board messages + Play music
while True:
    try:
        data = ser.readline().decode().strip() 
        if not data:
            continue  
        
        print(f"Received from Clue: {data}")  

        if data == "day":
            play_tracks(DAY_SIDE_TRACKS)
            alarm_playing = False  

        elif data == "night":
            play_tracks(NIGHT_SIDE_TRACKS)
            alarm_playing = False  

        elif data == "warning": 
                play_tracks(HEAT_WARNING_TRACK)
                alarm_playing = True  

        elif data == "pause_alarm":  
                sp.pause_playback(device_id=DEVICE_ID)
                alarm_playing = False  
                print("⏸️ Alarm Stopped.")

    except Exception as e:
        print(f"Serial Communication Error: {e}")
