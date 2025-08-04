#!/usr/bin/env python3
"""
Analyze OpenMATB session data to show correct vs incorrect key responses
"""
import csv
import sys
from datetime import datetime

RESPONSE_WINDOW_SECONDS = 10

def analyze_session(csv_file):
    failures = []
    keypresses = []
    
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row
        for row in reader:
            if len(row) >= 5:
                try:
                    timestamp = float(row[0])
                except ValueError:
                    continue  # Skip rows with invalid timestamps
                event_type = row[2]
                
                # Track failures
                if event_type == "event" and len(row) >= 6:
                    plugin = row[3]
                    action = row[4]
                    value = row[5]
                    
                    if plugin == "sysmon" and "failure" in action and value == "1":
                        # Extract which gauge failed (F1-F6)
                        if "scales-1" in action:
                            expected_key = "F1"
                        elif "scales-2" in action:
                            expected_key = "F2"
                        elif "scales-3" in action:
                            expected_key = "F3"
                        elif "scales-4" in action:
                            expected_key = "F4"
                        elif "lights-1" in action:
                            expected_key = "F5"
                        elif "lights-2" in action:
                            expected_key = "F6"
                        else:
                            expected_key = "UNKNOWN"
                        
                        failures.append({
                            'timestamp': timestamp,
                            'expected_key': expected_key,
                            'gauge': action
                        })
                
                # Track key presses
                if event_type == "input" and len(row) >= 6:
                    input_type = row[3]
                    key = row[4]
                    action = row[5]
                    
                    if input_type == "keyboard" and action == "release":
                        keypresses.append({
                            'timestamp': timestamp,
                            'key': key
                        })
    
    print(f"=== Session Analysis ===")
    print(f"File: {csv_file}")
    print(f"Total failures: {len(failures)}")
    print(f"Total key presses: {len(keypresses)}")
    print()
    
    # Match key presses to failures (within RESPONSE_WINDOW_SECONDS(ex:10) second window)
    correct_responses = 0
    incorrect_responses = 0
    missed_failures = 0
    false_alarms = 0
    
    print("=== Failure Analysis ===")
    
    for i, failure in enumerate(failures):
        failure_time = failure['timestamp']
        expected_key = failure['expected_key']
        
        # Find key presses within RESPONSE_WINDOW_SECONDS(ex:10) seconds after this failure
        response_found = False
        for keypress in keypresses:
            if (keypress['timestamp'] > failure_time and 
                keypress['timestamp'] <= failure_time + RESPONSE_WINDOW_SECONDS):
                
                if keypress['key'] == expected_key:
                    print(f"Failure {i+1:2d}: {failure['gauge']:20s} -> Expected {expected_key}, Got {keypress['key']} ✓ CORRECT")
                    correct_responses += 1
                    response_found = True
                    break
                else:
                    print(f"Failure {i+1:2d}: {failure['gauge']:20s} -> Expected {expected_key}, Got {keypress['key']} ✗ WRONG KEY")
                    incorrect_responses += 1
                    response_found = True
                    break
        
        if not response_found:
            print(f"Failure {i+1:2d}: {failure['gauge']:20s} -> Expected {expected_key}, Got NONE      ✗ MISSED")
            missed_failures += 1
    
    # Check for false alarms (key presses not matching any failure)
    for keypress in keypresses:
        key_time = keypress['timestamp']
        key = keypress['key']
        
        # Check if this keypress was a response to a failure
        was_response = False
        for failure in failures:
            if (key_time > failure['timestamp'] and 
                key_time <= failure['timestamp'] + RESPONSE_WINDOW_SECONDS):
                was_response = True
                break
        
        if not was_response:
            print(f"False Alarm: Key {key} pressed at {key_time:.1f}s with no corresponding failure")
            false_alarms += 1
    
    print()
    print("=== Summary ===")
    print(f"Correct responses: {correct_responses}")
    print(f"Wrong key responses: {incorrect_responses}")
    print(f"Missed failures: {missed_failures}")
    print(f"False alarms: {false_alarms}")
    print(f"Total accuracy: {correct_responses}/{len(failures)} = {correct_responses/len(failures)*100:.1f}%")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_session.py <session_file.csv>")
        sys.exit(1)
    
    analyze_session(sys.argv[1])