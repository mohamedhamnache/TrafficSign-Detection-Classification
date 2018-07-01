import os

for f in os.listdir("results"):
    if "ERROR" not in f:
        print(f)