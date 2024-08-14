#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""
import sys
import signal

# Count of each status code
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

total_size = 0
line_count = 0


def print_stats():
    """Printing statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def handle_interrupt(signal, frame):
    """keyboard interruption"""
    print_stats()
    sys.exit(0)


# Signal handler for CTRL + C
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 9:
            continue

        # Extracting file size & status code
        file_size = parts[-1]
        status_code = parts[-2]

        # Checking if file_size is number
        if not file_size.isdigit():
            continue
        total_size += int(file_size)

        # Increment status code count
        if status_code in status_codes:
            status_codes[status_code] += 1

        line_count += 1

        # Printing stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Printing stats on keyboard interruption
    print_stats()
    sys.exit(0)
