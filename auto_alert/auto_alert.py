#!/usr/bin/env python3
"""
Hardcoded Sound Alert System - simple timed alerts
"""

import time
import pyttsx3
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
    
    # Hardcoded schedule: (seconds_from_start, key_to_announce)
    # Based on testcase1_high_freq_study.txt but with some wrong recommendations
    schedule = [
        (10, "F1"),   # 0:00:10 scales-1-failure -> F1 (CORRECT)
        (20, "F5"),   # 0:00:20 lights-2-failure -> F6 but saying F5 (WRONG) 
        (30, "F3"),   # 0:00:30 scales-3-failure -> F3 (CORRECT)
        (40, "F5"),   # 0:00:40 lights-1-failure -> F5 (CORRECT)
        (50, "F1"),   # 0:00:50 scales-2-failure -> F2 but saying F1 (WRONG)
        (60, "F6"),   # 0:01:00 lights-2-failure -> F6 (CORRECT)
        (70, "F1"),   # 0:01:10 scales-1-failure -> F1 (CORRECT)
        (80, "F5"),   # 0:01:20 lights-1-failure -> F5 (CORRECT)
        (90, "F2"),   # 0:01:30 scales-3-failure -> F3 but saying F2 (WRONG)
        (100, "F6"),  # 0:01:40 lights-2-failure -> F6 (CORRECT)
        (110, "F1"),  # 0:01:50 scales-1-failure -> F1 (CORRECT)
    ]
    
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