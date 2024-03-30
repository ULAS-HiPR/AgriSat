# AgriSat

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
