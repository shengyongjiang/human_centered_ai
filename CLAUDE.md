# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Human-Centered AI final project studying **automation bias in human-in-the-loop systems** using the Multi-Attribute Task Battery (MATB). The project contains three main components:

1. **OpenMATB**: Open-source implementation of the Multi-Attribute Task Battery - a psychological testing framework for human-computer interaction research with four simultaneous tasks (monitoring, tracking, communications, resource management)
2. **Auto Alert System**: Companion alert system that provides timed audio cues using text-to-speech during experiments  
3. **Session Analysis Tools**: Python scripts to analyze participant performance and response patterns

## Commands

### Development Setup

```bash
# Install OpenMATB dependencies
cd OpenMATB
python -m pip install -r requirements.txt

# Auto alert system requires pyttsx3
pip install pyttsx3

# For visualizations
pip install matplotlib numpy
```

### Run Experiment Protocol

```bash
# 1. Start OpenMATB (wait at start screen)
cd OpenMATB
python main.py

# 2. In separate terminal, start alert system
cd auto_alert
python auto_alert.py

# 3. Begin experiment in OpenMATB (press space)
```

### Session Data Analysis

```bash
# Analyze individual session
python analyze_session.py <session_file.csv>

# Example
python analyze_session.py OpenMATB/sessions/2025-08-04/6_250804_175111.csv

# Generate visualizations (after running experiments)
python automation_bias_by_frequency.py
python performance_by_duration.py
```

### Test Case Development

```bash
# Update scenario in config.ini to switch test cases
# Available scenarios in OpenMATB/includes/scenarios/:
# - testcase1.txt (2min, 10s intervals)  
# - __testcase1_low_freq_study.txt (4min, 20s intervals)
# - testcase2.txt (8min, 10s intervals)
# - __testcase2_low_freq_study.txt (8min, 20s intervals)

# Update alert configuration in auto_alert/auto_alert.py FILE_NAME variable
```

### Compilation (Linux)

```bash
cd OpenMATB
./linux_compilation.sh
```

## Architecture

### Event-Driven Experiment Engine

**Core Architecture**: OpenMATB operates on a scenario-based event scheduler that coordinates multiple task plugins simultaneously. The system is designed for psychological research requiring precise timing and comprehensive logging.

**Key Components**:
- **Scheduler** (`core/scheduler.py`): Parses scenario files and triggers timed events
- **Plugin System** (`plugins/`): Independent task modules (sysmon, track, communications, resman, scheduling)
- **Logger** (`core/logger.py`): Captures all events to CSV format for analysis
- **Configuration** (`config.ini`): Controls scenario selection, display settings, localization

### Automation Bias Study Design

**Research Method**: Between-subjects design testing how alert frequency affects automation bias in multitasking environments. Two primary manipulations:

1. **Frequency Conditions**: 
   - High frequency: 10-second intervals
   - Low frequency: 20-second intervals

2. **Automation Accuracy Levels**:
   - 80% accurate alerts (20% wrong) 
   - 90% accurate alerts (10% wrong)

**Test Case Structure**:
- **TestCase1**: Shorter duration studies (2-4 minutes)
- **TestCase2**: Extended duration studies (8 minutes)
- Each test case has high/low frequency variants

### Data Flow and Analysis Pipeline

**Experiment Execution**:
1. Scenario files define failure events at specific timestamps
2. Auto alert system provides concurrent audio recommendations
3. All interactions logged to timestamped CSV files
4. Analysis scripts process logs to calculate performance metrics

**Key Mappings for System Monitoring**:
- `scales-1-failure` → F1, `scales-2-failure` → F2, `scales-3-failure` → F3, `scales-4-failure` → F4
- `lights-1-failure` → F5, `lights-2-failure` → F6
- Response window: 10 seconds (defined by `RESPONSE_WINDOW_SECONDS` constant)

**Performance Metrics**:
- Correct responses: First key press matches expected key within time window
- Incorrect responses: Wrong key pressed within time window
- Missed failures: No response within 10-second window
- False alarms: Key presses with no corresponding failure

### Alert System Integration

**Coordination Protocol**: External alert system provides audio cues that may conflict with visual task requirements to study automation bias effects.

**Configuration Files**:
- `testcase*_automation.json`: 100% accurate alerts (control condition)
- `testcase*_automation_bias_accurate_*_*.json`: Biased alerts with specified accuracy rates
- JSON format: `[{"time": seconds, "key": "F*", "comment": "description"}, ...]`

**Implementation Notes**:
- Uses pyttsx3 for text-to-speech "Press F1/F2/etc" alerts
- Must be started after OpenMATB initialization but before experiment begins
- Alert timing synchronized with scenario failure events

## Development Workflows

### Creating New Test Scenarios

1. **Scenario File**: Create new `.txt` file in `OpenMATB/includes/scenarios/`
2. **Alert Configuration**: Generate corresponding JSON file in `auto_alert/`
3. **Configuration**: Update `OpenMATB/config.ini` scenario_path
4. **Testing**: Run experiment and verify with `analyze_session.py`

### Automation Bias Configuration Generation

Alert configurations follow naming pattern: `testcase*_automation_bias_accurate_*_*.json` where final numbers indicate accuracy percentage (e.g., `10_90` = 90% accurate, 10% wrong).

### Result Analysis and Visualization

Session analysis follows this workflow:
1. Run experiments with different configurations
2. Use `analyze_session.py` to process individual sessions  
3. Update `result.md` with performance data
4. Generate comparative visualizations with provided Python scripts

## Important File Locations

- **Main Config**: `OpenMATB/config.ini` - display settings, scenario selection
- **Scenarios**: `OpenMATB/includes/scenarios/testcase*.txt` - experiment protocols  
- **Session Data**: `OpenMATB/sessions/YYYY-MM-DD/` - logged experiment data
- **Alert Schedules**: `auto_alert/testcase*_automation*.json` - timed alert configurations
- **Analysis Tools**: `analyze_session.py`, visualization scripts
- **Results**: `result.md` - performance summary table for analysis