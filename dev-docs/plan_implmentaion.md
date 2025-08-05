# Simple Automation Bias Study Implementation Plan

## Goal
Test how alert frequency affects automation bias in OpenMATB system monitoring task.

## Simple Approach

### 1. Create Test Case Scenarios

- **TestCase1 High Frequency**: `includes/scenarios/testcase1.txt` - alerts every 10 seconds
- **TestCase1 Low Frequency**: `includes/scenarios/__testcase1_low_freq_study.txt` - alerts every 20 seconds
- Both scenarios run for 2-4 minutes with the same total number of failures
- Additional test cases can be created following the same naming pattern 

### 2. A script adding automatic Sound Alert

- Add simple sound alerts when system failures occur
- Alert play sound: " Press F1" (or other key)
- Alert play sound is according from `includes/scenarios/testcase1.txt` ,`includes/scenarios/__testcase1_low_freq_study.txt` , Hoewver, it add some wrong hit sound, ex: use should press F1 key but sound play " Press F2"
- Make 80% of recommendations correct, 20% incorrect

### 3. Simple Data Collection

- Log when alert appears
- Log if user followed (pressed SPACE) or ignored (pressed ESC)
- Log if recommendation was correct or incorrect
- Calculate: % of incorrect recommendations followed = automation bias

### 4. Analysis

- Compare automation bias rate between high vs low frequency groups
- Export data to CSV for statistical analysis

## Files to Modify

1. `plugins/sysmon.py` - add alert popup system
2. `includes/scenarios/testcase1.txt` - create high frequency scenario
3. `includes/scenarios/__testcase1_low_freq_study.txt` - create low frequency scenario

## Test Case Structure
- **TestCase1**: Basic automation bias comparison (high vs low frequency)
- **TestCase2**: (Future) Different automation reliability levels
- **TestCase3**: (Future) Varying task difficulty
- **TestCase4**: (Future) Mixed modality alerts (visual + audio)

## Expected Outcome
Simple measurement showing whether people follow bad advice more often when alerts are frequent versus infrequent.