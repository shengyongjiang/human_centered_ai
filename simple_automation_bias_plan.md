# Simple Automation Bias Study Implementation Plan

## Goal
Test how alert frequency affects automation bias in OpenMATB system monitoring task.

## Simple Approach

### 1. Create Test Case Scenarios

- **TestCase1 High Frequency**: `testcase1_high_freq_study.txt` - alerts every 30-45 seconds
- **TestCase1 Low Frequency**: `testcase1_low_freq_study.txt` - alerts every 2-3 minutes
- Both scenarios run for 10 minutes with same total number of failures
- Additional test cases can be created following the same naming pattern
- 
### 2. Modify Existing System Monitoring

- Add simple popup alerts when system failures occur
- Alert shows: "RECOMMENDATION: Press F1" (or other key)
- User can press SPACE to follow or ESC to ignore
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
2. `includes/scenarios/testcase1_high_freq_study.txt` - create high frequency scenario
3. `includes/scenarios/testcase1_low_freq_study.txt` - create low frequency scenario

## Test Case Structure
- **TestCase1**: Basic automation bias comparison (high vs low frequency)
- **TestCase2**: (Future) Different automation reliability levels
- **TestCase3**: (Future) Varying task difficulty
- **TestCase4**: (Future) Mixed modality alerts (visual + audio)

## Expected Outcome
Simple measurement showing if people follow bad advice more often when alerts are frequent vs infrequent.