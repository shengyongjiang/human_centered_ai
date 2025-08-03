# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Human-Centered AI final project containing two main components:

1. **OpenMATB**: An open-source implementation of the Multi-Attribute Task Battery (MATB) - a psychological testing framework for human-computer interaction research
2. **AlertSystem**: A companion alert system built with pygame and pynput

## Common Commands

### OpenMATB
```bash
# Install dependencies (in OpenMATB directory)
python -m pip install -r requirements.txt

# Run the main application
python main.py

# Generate scenarios
python scenario_generator.py
```

### AlertSystem
```bash
# Install dependencies (in AlertSystem directory using uv)
uv sync

# Run with uv
uv run python [script_name].py
```

## Architecture

### OpenMATB Structure
- **Core Framework**: The `core/` directory contains the main engine components:
  - `scheduler.py`: Event scheduling and timing system
  - `window.py`: Main display window management
  - `scenario.py`: Scenario file parsing and execution
  - `logger.py`: Data logging functionality
  - `widgets/`: UI components (buttons, scales, tanks, etc.)

- **Plugin System**: The `plugins/` directory contains modular task implementations:
  - `sysmon.py`: System monitoring task
  - `track.py`: Tracking task
  - `communications.py`: Radio communications task
  - `resman.py`: Resource management task
  - `scheduling.py`: Task scheduling display
  - `instructions.py`: HTML instruction display
  - `performance.py`: Performance feedback system

- **Configuration**: 
  - `config.ini`: Main configuration file (language, screen settings, scenario selection)
  - Scenarios are defined in `includes/scenarios/` as text files with timed events
  - Session data is logged to `sessions/` directory as CSV files

### Key Design Patterns
- **Plugin Architecture**: Each task is implemented as a separate plugin inheriting from `AbstractPlugin`
- **Event-Driven System**: All actions are scheduled as events with timestamps in scenario files
- **Internationalization**: Support for multiple languages via gettext (locales in `locales/`)
- **Logging System**: Comprehensive logging of all user interactions and system states

### Data Flow
1. Configuration loaded from `config.ini`
2. Scenario file parsed into timed events
3. Scheduler executes events and manages plugin lifecycle
4. User interactions logged to CSV files in `sessions/`
5. Plugins communicate through the central scheduler

## Important Files
- `main.py`: Application entry point with language setup and KeyLogger integration
- `config.ini`: Configuration file specifying scenario, language, display settings
- `includes/scenarios/default_en.txt`: Default English scenario demonstrating all tasks
- `requirements.txt`: Python dependencies (pyglet, pylsl, rstr, pyparallel)

## Development Notes
- Uses pyglet for graphics rendering
- Supports joystick input for tracking tasks
- Includes Lab Streaming Layer (LSL) support for neurophysiological recordings
- Virtual environment should be named `.venv` for shebang compatibility
- Session data includes detailed performance metrics and timing information
- `grep -E "input,keyboard" "./sessions/date/session.csv"` get user input