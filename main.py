#! /usr/bin/python
# - * - coding: UTF - 8 - * -
from cmd.cmd_parse import ParseCmd


def main():
    cmd = ParseCmd()
    args = cmd.parse_cmd()
    cmd.execute_cmd(args)


if __name__ == "__main__":
    main()

