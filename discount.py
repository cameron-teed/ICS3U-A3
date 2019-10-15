#!usr/bin/env python

# Created by: Cameron Teed
# Created On: September 2019
# this program tells you your discounted price


def main():
    # this program tells you your discounted price

    number = int(input("Pleae put in your total: "))
    discount = number*.10
    tax = 0.13*number
    Total = number + tax - discount

    # process
    if number >= 1000:
        # output
        print("your total is ${}, with ${} in taxes and a ${} discount"
              .format(Total, tax, discount))

    # process
    if number < 1000:
        Total = number + tax
        # output
        print("You do not qualify for a discount, your total is ${}, with ${}"
              " in taxes".format(Total, tax))


if __name__ == "__main__":
    main()
