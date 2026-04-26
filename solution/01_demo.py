#!/usr/bin/env python
"""
Broken ML-like workload.

This script intentionally prints several lines of successful-looking output
before failing. The goal is to practice reading Slurm output carefully and
distinguishing application errors from scheduler errors.
"""
import random
import time
print("Starting training job...")
print("Loading synthetic training data...")
time.sleep(1)
loss = 1.0
for epoch in range(1, 6):
    loss *= random.uniform(0.70, 0.90)
    print(f"Epoch {epoch}: loss={loss:.4f}")
    time.sleep(1)
results = {"final_loss": round(loss, 4), "status": "success"}
print("Training complete.")
print(result)  # Intentional bug: should be 'results'
