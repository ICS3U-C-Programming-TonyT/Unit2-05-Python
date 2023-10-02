#!/usr/bin/env python3
# Created By: Tony Tran
# Date: Oct. 2, 2023
# This is program will scope out variable_X, variable_Y, variable_Z.

variable_x = 25


def local_variable() -> None:
    variable_x = 10
    variable_y = 30

    variable_x = variable_x + 1
    variable_z = variable_x + variable_y

    print(f"Local variable:  {variable_x} + {variable_y} = {variable_z}")


def global_variable() -> None:
    global variable_x
    variable_y = 30

    variable_x = variable_x + 1
    variable_z = variable_x + variable_y

    print(f"Global variable: {variable_x} + {variable_y} = {variable_z}")


def main() -> None:
    local_variable()
    global_variable()

    print("\nDone.")


if __name__ == "__main__":
    main()
