#!/bin/bash -e

echo "Installing necessary packages..."
pip install -r requirements.txt

echo "Starting AgriSat..."
python main.py