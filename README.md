# Smart Home Server

A Python Flask-based API and Web app for smart home automation, hosted on Raspberry Pi with custom circuitry built on a breadboard using a 433 MHz transmitter and receiver.

---

## **Features**

- RESTful API and web interface for controlling smart home lights.
- Runs on Raspberry Pi for affordable, low-power home automation.
- Integrates with custom-built hardware using 433 MHz RF modules (transmitter & receiver)
- Easily extensible for new devices and automation routines

---

## **Hardware Requirements**

- Raspberry Pi (any model with GPIO support)
- Breadboard and jumper wires
- 433 MHz RF transmitter and receiver modules
- Supported smart devices (e.g., RF-controlled outlets or switches)

---

## **Getting Started**

1. **Clone the repository:**
git clone https://github.com/yourusername/smart-home-server.git
cd smart-home-server

2. **Install dependencies:**
pip install -r requirements.txt

3. **Connect the hardware:**
- Wire the 433 MHz transmitter and receiver to your Raspberry Pi GPIO pins as described in the hardware section of the docs *<WIP>*.

4. **Run the server:**
python app.py
The web app and API will be available locally (default: http://localhost:5000).
