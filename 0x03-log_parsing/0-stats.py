#!/usr/bin/python3
"""
Log parsing - a script that reads stdin line by line and computes metrics:
    Input format:   <IP Address> - [<date>]
                    "GET /projects/260 HTTP/1.1" <status code> <file size>
    (if the format is not this one, the line must be skipped)
    After every 10 lines and/or a keyboard interruption (CTRL + C)
    print these statistics from the beginning:
        Number of lines by status code: possible status code:
            200, 301, 400, 401, 403, 404, 405 and 500
        if a status code doesn’t appear or is not an integer,
            don’t print anything for this status code
        format: <status code>: <number>
        status codes should be printed in ascending order
"""
import re
import sys
import signal


def print_statistics(size, statusCount):
    """
    Prints logged statistics
    """
    print("File size: {:d}".format(size))
    for key, value in sorted(statusCount.items()):
        print("{}: {:d}".format(key, value))


def main():
    """
    Reads stdin
    """
    count: int = 0
    size: int = 0
    statusCount = {}
    pattern = r'^(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "([^"]+)" (\d+) (\d+)$'

    def handle_interrupt(signum, frame):
        print_statistics(size, statusCount)
        sys.exit(0)

    signal.signal(signal.SIGINT, handle_interrupt)

    for line in sys.stdin:
        line = line.strip()
        if line == "exit":
            break

        match = re.match(pattern, line)

        if match:
            count += 1
            if str(int(match.group(5))) == match.group(5):
                size = size + int(match.group(5))
            if str(int(match.group(4))) == match.group(4):
                if str(match.group(4)) in statusCount:
                    statusCount[str(match.group(4))] = statusCount[
                            str(match.group(4))] + 1
                else:
                    statusCount[str(match.group(4))] = 1

        if count % 10 == 0:
            print_statistics(size, statusCount)

    print_statistics(size, statusCount)


if __name__ == "__main__":
    main()
