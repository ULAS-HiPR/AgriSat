#!/bin/bash -e

rm -rf logs/*
rm -rf records/*

echo "Activating env..."
source ../env/bin/activate

echo "Starting AgriSat..."
python main.py