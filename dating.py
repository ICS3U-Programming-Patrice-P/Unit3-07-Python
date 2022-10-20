#!/usr/bin/env python3

# Created by: Patrice Pat-Odita
# Created on: oct 19 2022
# This program checks the qualification of a user to date the grandchild
# using compound boolean expression


def main():

    # Get user input
    user_wealth_input = input("Are you rich?(y/n): ")
    user_looks_input = input("Are you good looking?(y/n): ")
    print("")

    # Check if the user qualification
    if (
        user_wealth_input == "Y"
        or user_wealth_input == "y"
        or user_looks_input == "Y"
        or user_looks_input == "y"
    ):
        print("You can date our grandchild!")
        print("\033[1;35;39mThanks for playing")
    elif (
        user_wealth_input == "N"
        or user_wealth_input == "n"
        and user_looks_input == "N"
        or user_looks_input == "n"
    ):
        print("You can not date our grandchild.")
        print("\033[1;35;39mThanks for playing")
    else:
        print("Please enter either y/n.")
    print("\033[1;35;39mThanks for playing")


if __name__ == "__main__":
    main()
