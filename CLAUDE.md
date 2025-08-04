# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Human-Centered AI final project containing two main components:

1. **OpenMATB**: An open-source implementation of the Multi-Attribute Task Battery (MATB) - a psychological testing framework for human-computer interaction research
2. **AlertSystem**: A companion alert system built with pygame and pynput
3. **Session Analysis**: `analyze_session.py` - Analyzes OpenMATB session data to show correct vs incorrect key responses

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
```

## Architecture

### OpenMATB Structure
- **Configuration**: 
  - `config.ini`: Main configuration file (language, screen settings, scenario selection)
  - Scenarios are defined in `includes/scenarios/` as text files with timed events
  - Session data is logged to `sessions/` directory as CSV files

### Session Analysis
- `analyze_session.py`: Analyzes session CSV files to calculate response accuracy
- Uses `RESPONSE_WINDOW_SECONDS = 10` constant for failure response time window
- Tracks correct responses, incorrect responses, missed failures, and false alarms

# important-instruction-reminders
Do what has been asked; nothing more, nothing less.
NEVER create files unless they're absolutely necessary for achieving your goal.
ALWAYS prefer editing an existing file to creating a new one.
NEVER proactively create documentation files (*.md) or README files. Only create documentation files if explicitly requested by the User.