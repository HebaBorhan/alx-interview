#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""
import re
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

pattern = re.compile(
    r'^'
    r'(\d+\.\d+\.\d+\.\d+)'
    r' - '
    r'\[([^\]]+)\]'
    r' "GET /projects/260 HTTP/1.1"'
    r' (\d{3})'
    r' (\d+)$'
)

try:
    for line in sys.stdin:
        match = pattern.match(line)
        if match:
            # Extracting status code and file size
            status_code = match.group(3)
            file_size = match.group(4)

            # Check if file_size is a number
            if file_size.isdigit():
                total_size += int(file_size)

                # Increment the count for the status code
                if status_code in status_codes:
                    status_codes[status_code] += 1

                line_count += 1

                # Print statistics every 10 lines
                if line_count % 10 == 0:
                    print_stats()

except KeyboardInterrupt:
    # Handle keyboard interruption
    print_stats()
    sys.exit(0)

# Print stats one last time if there are remaining lines
if line_count % 10 != 0:
    print_stats()
