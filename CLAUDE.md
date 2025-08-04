# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Human-Centered AI final project studying **automation bias in human-in-the-loop systems** using the Multi-Attribute Task Battery (MATB). The project contains three main components:

1. **OpenMATB**: Open-source implementation of the Multi-Attribute Task Battery - a psychological testing framework for human-computer interaction research with four simultaneous tasks (monitoring, tracking, communications, resource management)
2. **Auto Alert System**: Companion alert system that provides timed audio cues using text-to-speech during experiments  
3. **Session Analysis Tools**: Python scripts to analyze participant performance and response patterns

## Commands

### Run OpenMATB

```bash
uv run python start.py
```

### Run AlertSystem

```bash
uv run python auto_alert.py
```

### Analyze Session Data

```bash
python analyze_session.py <session_file.csv>

# Example
python analyze_session.py OpenMATB/sessions/2025-08-03/1_250803_155525.csv
```

### Compilation (Linux)

```bash
cd OpenMATB
./linux_compilation.sh
```

### Configuration and Data Flow

**Scenario Execution**: Text files in `includes/scenarios/` define timed events using format: `HH:MM:SS;module;command;parameters`

**Session Logging**: All interactions logged to `sessions/YYYY-MM-DD/SessionID.csv` with columns: `logtime,totaltime,scenario_time,type,module,address,value`

**Key Mappings** for system monitoring failures:
- `scales-1-failure` → F1, `scales-2-failure` → F2, etc.
- `lights-1-failure` → F5, `lights-2-failure` → F6
- Response window: 10 seconds (defined by `RESPONSE_WINDOW_SECONDS` constant)

### Auto Alert Integration

**Coordination Protocol**: The alert system reads JSON schedule files with precise timing to provide audio cues that may influence participant responses (studying automation bias).

**Technical Details**:
- Uses pyttsx3 for text-to-speech "Press F1/F2/etc" alerts
- JSON schedule format: `[{"time": seconds, "key": "F1"}, ...]`
- Must be started after OpenMATB but before experiment begins

### Session Analysis Engine

**Performance Metrics Calculation**:
- Parses CSV logs to extract failure events and keyboard responses
- Matches responses to failures within time windows
- Categorizes as: correct, incorrect, missed, or false alarm
- Outputs accuracy statistics and detailed failure analysis

## Important File Locations

- **Main Config**: `OpenMATB/config.ini` - display settings, scenario selection
- **Scenarios**: `OpenMATB/includes/scenarios/` - experiment protocols  
- **Session Data**: `OpenMATB/sessions/YYYY-MM-DD/` - logged experiment data
- **Alert Schedules**: `auto_alert/*.json` - timed alert configurations
- **Analysis Tool**: `analyze_session.py` - performance analysis script