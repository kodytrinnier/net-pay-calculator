import time
import sys


def print_menu():
    print(30 * "-" + "MENU" + 30 * "-")
    print(22 * "-" + "Net Income Calculator" + 21 * "-")
    print("1. Annual")
    print("2. Monthly")
    print("3. BiWeekly")
    print("4. Exit Program")
    print(65 * "-")


def print_menu_income():
    print(30 * "-" + "MENU" + 30 * "-")
    print(22 * "-" + "Net Income Calculator" + 21 * "-")
    print("1. Hourly")
    print("2. Salary")
    print("3. Exit Program")
    print(65 * "-")


def get_income_type():
    loop = True
    while loop:
        print_menu_income()
        choice = input("Are you paid hourly or salary? [1-3]: ")
        if choice == "1":
            print("\nHourly has been selected\n")
            itype = 0
            return itype
        elif choice == "2":
            print("\nSalary has been selected\n")
            itype = 1
            return itype
        elif choice == "3":
            print("\nExiting...\n")
            sys.exit(0)
        else:
            print("\nWrong option selection. Please enter a valid menu option...\n")
            time.sleep(1)


def get_income():
    itype = get_income_type()
    if itype == 0:
        x = 0
        while x == 0:
            try:
                hourly = input('How much do you make an hour: ')
                hourly = hourly.lstrip('$')
                hourly = float(hourly)
                salary = hourly * 2080
                return int(salary)
            except NameError as err:
                print('Handling NameError:', err)
                raise
            except ValueError as valerr:
                print('Handling ValueError:', valerr)
                raise
    else:
        x = 0
        while x == 0:
            try:
                salary = input('How much do you make a year: ')
                if 'k'.casefold() in salary.casefold():
                    salary = salary.rstrip('k')
                    salary = salary.rstrip('K')
                    salary = salary.lstrip('$')
                    salary = int(salary) * 1000
                    return salary
                salary = salary.lstrip('$')
                salary = int(salary)
                return int(salary)
            except NameError as err:
                print('Handling NameError:', err)
                raise


def get_tax_bracket(salary):
    if salary <= 9525:
        bracket = .90
        tax_owed = 0
    if 9526 <= salary <= 38700:
        bracket = .88
        tax_owed = 952.5
    if 38701 <= salary <= 82500:
        bracket = .78
        tax_owed = 4453.5
    if 82501 <= salary <= 157500:
        bracket = .76
        tax_owed = 14089.5
    if 157501 <= salary <= 200000:
        bracket = .68
        tax_owed = 32089.5
    if 200001 <= salary <= 500000:
        bracket = .65
        tax_owed = 45689.5
    if salary > 500000:
        bracket = .63
        tax_owed = 150689.5
    return bracket, tax_owed


def get_net_income():
    salary = get_income()
    bracket, tax_owed = get_tax_bracket(salary)
    net_income = (salary - tax_owed) * bracket
    return int(net_income)


def net_monthly():
    net = get_net_income()
    monthly = net / 12
    return int(monthly)


def net_biweekly():
    monthly = net_monthly()
    biweekly = monthly / 2
    return int(biweekly)


def main():
    loop = True
    while loop:
        print_menu()
        choice = input("For which timeframe would you like to calculate your net income? [1-4]: ")
        if choice == "1":
            print("\nAnnual has been selected\n")
            annual = get_net_income()
            print("\nYour net annual income is ${}\n".format(annual))
            loop = False
        elif choice == "2":
            print("\nMonthly has been selected\n")
            monthly = net_monthly()
            print("\nYour net monthly income is ${}\n".format(monthly))
            loop = False
        elif choice == "3":
            print("\nBiWeekly has been selected\n")
            biweekly = net_biweekly()
            print("\nYour net BiWeekly income is ${}\n".format(biweekly))
            loop = False
        elif choice == "4":
            print("\nExiting...\n")
            sys.exit(0)
        else:
            print("\nWrong option selection. Please enter a valid menu option...\n")
            time.sleep(1)


main()
