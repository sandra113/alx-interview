#!/usr/bin/python3


import sys
import signal

def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

def print_statistics():
    total_size = sum(file_sizes)
    print("Total file size:", total_size)
    for status_code, count in sorted(status_code_counts.items()):
        print(f"{status_code}: {count}")

def process_line(line):
    parts = line.split()
    if len(parts) != 7:
        return
    try:
        status_code = int(parts[4])
        file_size = int(parts[5])
    except ValueError:
        return
    if status_code not in status_code_counts:
        status_code_counts[status_code] = 0
    status_code_counts[status_code] += 1
    file_sizes.append(file_size)

status_code_counts = {}
file_sizes = []

signal.signal(signal.SIGINT, signal_handler)

try:
    for i, line in enumerate(sys.stdin, start=1):
        process_line(line.strip())
        if i % 10 == 0:
            print_statistics()
except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)

