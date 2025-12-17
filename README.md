# Log Analysis Tool

## Overview
This project parses raw system logs and produces a structured summary of operational events.
It simulates how engineers monitor systems, detect anomalies, and identify recurring failures.

## Features
- Parses unstructured log data
- Aggregates event counts
- Identifies repeated error messages
- Outputs a human-readable summary report

## Assumptions
- Logs follow a consistent timestamp + level format
- Batch processing is sufficient for this use case

## Future Improvements
- Support streaming logs
- Add severity thresholds
- Visualize trends over time
