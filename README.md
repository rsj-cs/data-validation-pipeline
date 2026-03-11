# Data Validation Pipeline

## Overview
An automated data validation pipeline that processes records, detects 
corrupt or invalid data, and produces a detailed integrity report. 
Built in Python using core data validation concepts directly relevant 
to distributed systems and data pipeline research.

## What It Does
- Generates a batch of records with intentionally mixed clean/corrupt data
- Runs each record through a multi-rule validation engine
- Separates clean records from rejected ones
- Produces a full report showing pass rate and exact errors per record

## Validation Rules
| Rule | Condition |
|------|-----------|
| Age check | Must be between 0 and 99 |
| Salary check | Must be non-negative |
| Name check | Cannot be empty |

## Sample Output
