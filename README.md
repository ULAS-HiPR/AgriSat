# AgriSat

This project is the operations for data processing and analysis of satellite images for agriculture from a CanSat running a Raspberry Pi at the edge. For parallelism we use child processes via sensor `clients` and using `handlers` for logging, persistence and data processing.

## Installation

```bash
git clone https://github.com/ULAS-HiPR/AgriSat.git
cd AgriSat

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Testing

```bash
coverage run --source=clients,handlers -m unittest discover -s tests
coverage report
```

### Coverage metrics

| Name                       |    Stmts |     Miss |   Cover |
|--------------------------- | -------: | -------: | ------: |
| clients/AltimeterClient.py |       18 |       18 |      0% |
| clients/BaseClient.py      |       16 |       16 |      0% |
| clients/CameraClient.py    |       18 |       18 |      0% |
| clients/GpsClient.py       |       19 |       19 |      0% |
| clients/LoraClient.py      |       14 |       14 |      0% |
| clients/NetClient.py       |        9 |        9 |      0% |
| handlers/CSVHandler.py     |       12 |        0 |    100% |
| handlers/LogHandler.py     |       29 |        0 |    100% |
| handlers/\_\_init\_\_.py   |        0 |        0 |    100% |
|                  **TOTAL** |  **135** |   **94** | **30%** |
