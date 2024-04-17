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
coverage run -m unittest discover -s tests
coverage report
```

### Coverage metrics
| Name                      |    Stmts |     Miss |   Cover |
|-------------------------- | -------: | -------: | ------: |
| handlers/CSVHandler.py    |       12 |        0 |    100% |
| handlers/LogHandler.py    |       29 |        0 |    100% |
| handlers/\_\_init\_\_.py  |        0 |        0 |    100% |
| tests/test\_CSVHandler.py |       32 |        1 |     97% |
| tests/test\_LogHandler.py |       48 |        1 |     98% |
|                 **TOTAL** |  **121** |    **2** | **98%** |
