# DuneTunes 🎵🌡️  

**DuneTunes** is a temperature-driven telltale designed for **desert environments**, where extreme temperature fluctuations occur between day and night. This project utilizes an **Adafruit Clue board**, **CircuitPython**, and the **Spotify API** to create an adaptive experience by playing music based on temperature conditions, while also alerting users to extreme heat.

## **Features**
- **Live Temperature & Humidity Display** – Uses the Clue board's built-in sensors.
- **Day & Night Music Mode** – Plays **Day Side** or **Night Side** tracks from *Night and Day* by Joe Jackson, based on temperature thresholds.
- **Extreme Heat Warning** – If the temperature exceeds **30°C** (configurable), it flashes a warning on-screen and plays an alarm track via **Spotify**.
- **User Interaction** – Pressing **Button A** stops the alarm.

## **🛠️ Hardware & Software Requirements**
### **🔹 Hardware**
- **Adafruit Clue board**
- **USB Type C to Micro B cable**
- **LiPo battery** (for portable use)

### **🔹 Software**
- **CircuitPython** (installed on the Clue board)
- **Mu Editor** (for writing and flashing code)
- **Python 3.x** (for running the laptop-side script)
- **Spotipy** (Spotify Web API library)

## **🖥️ How It Works**
1. The Clue board **continuously reads the temperature**.
2. It **sends temperature data via Serial** to a connected laptop.
3. A **Python script on the laptop** listens for this data and controls playback using the **Spotify API**.
4. **Different temperature ranges trigger different modes**:
   - **Above 25°C → "Day Side" tracks play**
   - **Below 25°C → "Night Side" tracks play**
   - **Above 30°C → Alarm track plays + LED flashes**
5. The user can **press Button A** to stop the alarm.

## **Installation & Setup**
### **Set Up the Clue Board**
- Install **CircuitPython** on the Clue board: [Guide](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython)
- Install **Mu Editor** for writing & flashing the CircuitPython script.

### **Clone This Repository**
```sh
git clone https://github.com/yourusername/dunetunes.git
cd dunetunes
