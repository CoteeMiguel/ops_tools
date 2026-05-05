# Operations Tools

> A collection of desktop utilities and automation scripts for the supply chain team's daily workflow. Small scripts with high day-to-day impact: from opening a delivery's tracking page with a keyboard shortcut to calculating KPIs across hundreds of records in seconds.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)

---

## Tools

### `dlvsearcher.py` + `dlv.bat` — One-click delivery tracking
Opens the Global Logistics Provider's TMS tracking page for any delivery number currently in your clipboard. Triggered from anywhere in Windows via the `.bat` shortcut — no browser navigation, no copy-pasting into search fields.

**Usage:**
1. Copy a delivery number (`Ctrl+C`)
2. Run `dlv.bat` (or assign a keyboard shortcut to it in Windows)
3. Browser opens directly on that delivery's tracking page

```python
# The entire script — maximum simplicity, maximum utility
import pyperclip, webbrowser
webbrowser.open(TMS_TRACKING_URL.format(pyperclip.paste()))
```

**Why it matters:** The team was manually looking up 20–50 deliveries per day in the TMS. This script eliminated that navigation overhead entirely.

---

### `kpi_ingreso.py` — LSP entry time KPI calculator
Analyzes LSP warehouse entry times at the hour and minute level to calculate punctuality KPIs across large datasets in seconds. Combines two separate date and time columns, calculates the delta between scheduled reception and actual entry time, and outputs descriptive statistics for the KPI.

**Stack:** Python · pandas  
**Input:** Entry report with columns `F/RECEPCION`, `HORA`, `F/INGRESO`, `HORA.1`

---

## Setup

```bash
git clone https://github.com/CoteeMiguel/ops-tools
cd ops-tools
pip install -r requirements.txt
```

To use `dlvsearcher` as a system-wide shortcut on Windows:

```
# Option 1: run directly
python dlvsearcher.py

# Option 2: double-click dlv.bat (edit the path inside the .bat first)

# Option 3: right-click the .bat → Create shortcut → Properties → Shortcut key
#            Assign any key combination (e.g. Ctrl+Alt+D)
```

---

## Dependencies

```
pyperclip
pandas
python-dotenv
```

---

## Author

**Jose Miguel Varas**  
Supply Chain & Operations Automation
[linkedin.com/in/jmvaras](https://linkedin.com/in/jmvaras) · [github.com/CoteeMiguel](https://github.com/CoteeMiguel)
