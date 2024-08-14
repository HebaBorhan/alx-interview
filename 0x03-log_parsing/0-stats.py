#!/usr/bin/python3
"""Unlock boxes"""
import sys
import signal

# Dictionary to hold the count of each status code
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
    """ Print the statistics """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def handle_interrupt(signal, frame):
    """ Handle keyboard interruption (CTRL + C) """
    print_stats()
    sys.exit(0)


# Setup signal handler for CTRL + C
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        # Expected format: <IP Address> - [<date>]
        # "GET /projects/260 HTTP/1.1" <status code> <file size>
        parts = line.split()
        if len(parts) < 9:
            continue

        # Extracting the file size and status code
        file_size = parts[-1]
        status_code = parts[-2]

        # Checking if file_size is a number
        if not file_size.isdigit():
            continue
        total_size += int(file_size)

        # Increment status code count if it's valid
        if status_code in status_codes:
            status_codes[status_code] += 1

        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print stats on keyboard interrupt
    print_stats()
    sys.exit(0)
