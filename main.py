#! /usr/bin/python
# - * - coding: UTF - 8 - * -
from analyzer.cmd import cmd_parse
from analyzer.cmd import cmd_execute


def main():
    args = cmd_parse.parse_cmd()
    cmd = cmd_execute.ExecuteCmd()
    cmd.execute_cmd(args)


if __name__ == "__main__":
    main()

