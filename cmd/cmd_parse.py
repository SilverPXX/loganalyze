# - * - coding: UTF - 8 - * -
import argparse
import sys


def parse_cmd():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--log_file', help='log file path',
                        required=True)
    parser.add_argument('-t', '--type', help='output report type',
                        choices=['all', 'ip', 'article', 'full'],
                        action='append', required=True)
    parser.add_argument('-u', '--url', help='log source url')

    flags, unparsed = parser.parse_known_args(sys.argv[1:])
    return flags
