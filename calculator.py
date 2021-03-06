import time
import sys
sys.tracebacklimit = 0

class Menu():
    def __init__(self, option1, option2, option3, option4):
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.option5 = option5


    def print_menu(self, option1="", option2="", option3="", option4="", option5=""):
        print(30 * "-" + "MENU" + 30 * "-")
        print(22 * "-" + "Net Income Calculator" + 21 * "-")
        if option1:
            print("{}".format(option1))
        if option2:
            print("{}".format(option2))
        if option3:
            print("{}".format(option3))
        if option4:
            print("{}".format(option4))
        if option5:
            print("{}".format(option5))
        print(65 * "-")


def get_income_type():
    loop = True
    while loop:
        print_menu_income = Menu.print_menu("", "1. Hourly", "2. Salary", "3. Exit")
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
            except (NameError,ValueError) as err:
                raise err
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
            except (NameError,ValueError) as err:
                raise err


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


def net_hourly():
    monthly = net_monthly()
    hourly = monthly / 160
    return int(hourly)


def main():
    loop = True
    while loop:
        income_menu = Menu.print_menu("", "1. Annual", "2. Hourly", "3. Monthly", "4. BiWeekly", "5. Exit")
        choice = input("For which timeframe would you like to calculate your net income? [1-5]: ")
        if choice == "1":
            print("\nAnnual has been selected\n")
            annual = get_net_income()
            print("\nYour net annual income is ${}\n".format(annual))
            loop = False
        elif choice == "2":
            print("\nHourly has been selected\n")
            hourly = net_hourly()
            print("\nYour net hourly income is ${}\n".format(hourly))
            loop = False
        elif choice == "3":
            print("\nMonthly has been selected\n")
            monthly = net_monthly()
            print("\nYour net Monthly income is ${}\n".format(monthly))
            loop = False
        elif choice == "4":
            print("\nBiWeekly has been selected\n")
            biweekly = net_biweekly()
            print("\nYour net BiWeekly income is ${}\n".format(biweekly))
            loop = False
        elif choice == "5":
            print("\nExiting...\n")
            sys.exit(0)
        else:
            print("\nWrong option selection. Please enter a valid menu option...\n")
            time.sleep(1)


main()
