#! /usr/bin/python
# - * - coding: UTF - 8 - * -
from cmd.cmd_parse import ParseCmd


def main():
    cmd = ParseCmd()
    cmd.parse_cmd()


if __name__ == "__main__":
    main()

