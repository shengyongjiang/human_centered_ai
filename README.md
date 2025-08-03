# Development Notes

## How to Add more scenarios

Scenarios in OpenMATB define the timing and sequence of events during a study session. They are text files located in `OpenMATB/includes/scenarios/` that use a specific format to control task behavior.

### Creating a New Scenario

1. **Create scenario file**: Add a new `.txt` file in `OpenMATB/includes/scenarios/`

2. **Define the scenario**: Use the format above to schedule events

3. **Configure OpenMATB**: Edit `OpenMATB/config.ini` to use your scenario:

   ```ini
   scenario_path=your_scenario_name.txt
   ```

## How to launch a new task test

   - In one terminal, go to folder of OpenMATB and run `python main.py`, **WAIT at the screen** of 'press space to start, switch to another terminal
   - In another terminal,  go to folder of `auto_alert` and run `python auto_alert.py`
   - START task


## How to check the anticipate key press log

All logs file save at `OpenMATB/sessions/` folder, ex:
OpenMATB/sessions/2025-01-15/1_250115_143022.csv

## Session Analysis Tool

- Analyzes OpenMATB session CSV files to evaluate user performance
- Maps system monitoring failures to expected key responses
- Tracks user key presses and matches them to failures
- Provides detailed performance metrics

### Usage

```bash
python analyze_session.py <session_file.csv>

## Example:
python analyze_session.py OpenMATB/sessions/2025-08-03/1_250803_155525.csv

# or to get user keypress by directly 
# grep -E "input,keyboard" "./sessions/date/session.csv"
```

### Key Mapping

- `scales-1-failure` → F1 (leftmost scale)
- `scales-2-failure` → F2 (second scale)
- `scales-3-failure` → F3 (third scale) 
- `scales-4-failure` → F4 (rightmost scale)
- `lights-1-failure` → F5 (left light, normally green)
- `lights-2-failure` → F6 (right light, normally off)

### Analysis Logic

- **Response Window**: 10 seconds after each failure
- **First Response Only**: Only the first key press within the window is evaluated
- **No Second Chances**: Self-correction attempts are ignored
- **Timeout**: No response within 10 seconds = MISS

### Output Metrics

- **Correct responses**: First key press matches expected key
- **Wrong key responses**: First key press is incorrect 
- **Missed failures**: No key press within 10-second window
- **False alarms**: Key presses with no corresponding failure
- **Total accuracy**: Correct responses / Total failures

### Sample Output

```
=== Session Analysis ===
File: sessions/2025-08-03/1_250803_155525.csv
Total failures: 23
Total key presses: 36

=== Failure Analysis ===
Failure  1: scales-1-failure     -> Expected F1, Got F1 ✓ CORRECT
Failure  2: lights-2-failure     -> Expected F6, Got F6 ✓ CORRECT
...

=== Summary ===
Correct responses: 16
Wrong key responses: 7
Missed failures: 0
False alarms: 0
Total accuracy: 16/23 = 69.6%
```

### Implementation Notes

- Parses CSV row format: `timestamp,relative_time,event_type,plugin,action,value`
- Extracts failure events where `plugin=sysmon` and `action` contains `failure` and `value=1`
- Tracks keyboard releases (`input,keyboard,KEY,release`)
- Uses chronological matching within time windows