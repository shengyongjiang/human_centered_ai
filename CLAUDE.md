# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Human-Centered AI final project containing two main components:

1. **OpenMATB**: An open-source implementation of the Multi-Attribute Task Battery (MATB) - a psychological testing framework for human-computer interaction research
2. **AlertSystem**: A companion alert system built with pygame and pynput

## AlertSystem
```bash
# Install dependencies (in AlertSystem directory using uv)
uv sync

# Run with uv
uv run python [script_name].py
```

## Architecture

### OpenMATB Structure

- **Configuration**: 
  - `config.ini`: Main configuration file (language, screen settings, scenario selection)
  - Scenarios are defined in `includes/scenarios/` as text files with timed events
  - Session data is logged to `sessions/` directory as CSV files

