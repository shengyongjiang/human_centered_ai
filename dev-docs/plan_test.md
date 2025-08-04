# Test Case Memory and Progress

## Completed Test Cases

### TestCase0: Alert Frequency vs Automation Bias

- **Status**: Scenarios created
- **Files**:
  - `testcase0_high_freq_study.txt` - High frequency alerts (10s intervals), 2 minutes total
  - `testcase0_low_freq_study.txt` - Low frequency alerts (20s intervals), 4 minutes total
- **Purpose**: Compare automation bias rates between different alert frequencies
- **Implementation**: Basic system monitoring with popup recommendations

### TestCase1: Alert Frequency vs Automation Bias

- **Status**: Scenarios created
- **Files**: 
  - `testcase1_very_high_freq_study.txt` - High frequency alerts (10s intervals), 2 minutes total
  - `testcase1_low_freq_study.txt` - Low frequency alerts (20s intervals), 4 minutes total
- **Purpose**: Compare automation bias rates between different alert frequencies
- **Implementation**: Basic system monitoring with popup recommendations


### TestCase2: Alert Frequency vs Automation Bias

- **Status**: Scenarios created
- **Files**: 
  - `testcase2_very_high_freq_study.txt` - High frequency alerts (10s intervals), 8 minutes total
  - `testcase2_low_freq_study.txt` - Low frequency alerts (20s intervals), 8 minutes total
- **Purpose**: Compare automation bias rates between different alert frequencies
- **Implementation**: Basic system monitoring with popup recommendations

## Plan Test Cases
### TestCase3: Automation Reliability Levels
- **Purpose**: Test how reliability affects trust and bias
- **Conditions**: 95% vs 70% vs 50% accuracy rates
- **Status**: Not started

### TestCase4: Task Difficulty Variations
- **Purpose**: Examine bias under different cognitive load conditions
- **Conditions**: Simple vs complex multi-task scenarios
- **Status**: Not started

### TestCase5: Multi-Modal Alerts
- **Purpose**: Compare visual vs audio vs combined alert effectiveness
- **Conditions**: Visual-only vs Audio-only vs Combined alerts
- **Status**: Not started

## Naming Convention
- Scenario files: `testcase[N]_[condition]_study.txt`
- Session logs: Stored in `sessions/[date]/` with test case identifier
- Analysis scripts: `analyze_testcase[N].py` (when created)