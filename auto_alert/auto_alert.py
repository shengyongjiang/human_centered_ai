#!/usr/bin/env python3
"""
Hardcoded Sound Alert System - simple timed alerts
"""

import time
import pyttsx3
import json
from datetime import datetime

def play_sound(key):
    """Play sound alert using text-to-speech"""
    tts = pyttsx3.init()
    tts.setProperty('rate', 150)
    tts.setProperty('volume', 0.9)
    
    message = f"Press {key}"
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Playing: {message}")
    
    tts.say(message)
    tts.runAndWait()

def run_hardcoded_alerts():
    """Run hardcoded sound alerts with timing"""
    
    with open('automation_bias_accurate_20_80.json', 'r') as f:
        schedule_data = json.load(f)
    
    schedule = [(item['time'], item['key']) for item in schedule_data]
    
    print("Hardcoded Sound Alert System")
    print(f"Total alerts: {len(schedule)}")
    print("Starting in 3 seconds...")
    time.sleep(3)
    
    start_time = time.time()
    
    for alert_time, key in schedule:
        # Wait until it's time for this alert
        target_time = start_time + alert_time
        current_time = time.time()
        
        if current_time < target_time:
            sleep_time = target_time - current_time
            print(f"Waiting {sleep_time:.1f}s for next alert...")
            time.sleep(sleep_time)
        
        play_sound(key)

def main():
    try:
        run_hardcoded_alerts()
        print("All alerts completed!")
    except KeyboardInterrupt:
        print("\nStopped by user.")

if __name__ == "__main__":
    main()