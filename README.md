# Amortized Analysis

A Python dynamic array that doubles its capacity when full and tracks the cost of each insertion. The cost model counts one operation for insertion and one for each copied element, excluding allocation and printing.

The example inserts eight values with a total cost of 15, averaging 1.875 operations per insertion. Resizing takes O(n) time, while insertion has O(1) amortized cost.

```bash
python amortized_analysis.py
```
