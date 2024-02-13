import sys

def parse_money(money_str):
    """
    Parses the money given in the string and represents it in a physical dollar, quarter, and cents print.

    Args:
        money_str (str): string represents the amount of money that is going to be parsed

    Raises:
        ValueError: If the money string is in the wrong format
    """
    try:
        dollars, cents = map(int, money_str[1:].split('.'))
    except ValueError:
        raise ValueError("Incorrect format. Please use the format '$X.YZ' ")

    total_cents = dollars * 100 + cents

    dollar_count = total_cents // 100
    total_cents %= 100

    quarter_count = total_cents // 25
    total_cents %= 25

    dime_count = total_cents // 10
    total_cents %= 10

    nickel_count = total_cents // 5
    total_cents %= 5

    penny_count = total_cents

    if dollar_count:
        print(f"{dollar_count} dollar{'s' if dollar_count > 1 else ''}")
    if quarter_count:
        print(f"{quarter_count} quarter{'s' if quarter_count > 1 else ''}")
    if dime_count:
        print(f"{dime_count} dime{'s' if dime_count > 1 else ''}")
    if nickel_count:
        print(f"{nickel_count} nickel{'s' if nickel_count > 1 else ''}")
    if penny_count:
        print(f"{penny_count} penny{'s' if penny_count > 1 else ''}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Incorrect format. python3 program1.py '$X.YZ' ")
        sys.exit(1)

    money_str = sys.argv[1]
    parse_money(money_str)
