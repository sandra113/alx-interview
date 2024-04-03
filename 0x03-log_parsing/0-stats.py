#!/usr/bin/python3

import sys
import signal

# Initialize variables
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    print("Total file size:", total_file_size)
    for status_code in sorted(status_code_counts.keys()):
        if status_code_counts[status_code] > 0:
            print(f"{status_code}: {status_code_counts[status_code]}")

def process_line(line):
    global total_file_size, line_count
    parts = line.split()
    if len(parts) != 10 or parts[5] != '"GET':
        return
    try:
        status_code = int(parts[8])
        file_size = int(parts[9])
        total_file_size += file_size
        status_code_counts[status_code] += 1
        line_count += 1
    except ValueError:
        pass

def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        process_line(line)
        if line_count % 10 == 0:
            print_statistics()
except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)

