"""
Working Capital Analyzer
Calculates DIO, DSO, DPO and Cash Conversion Cycle.
Author: Ashutosh
"""

def safe_division(numerator, denominator):
    if denominator == 0:
        return 0
    return numerator / denominator


def calculate_dio(inventory, cogs):
    return safe_division(inventory, cogs) * 365


def calculate_dso(receivables, revenue):
    return safe_division(receivables, revenue) * 365


def calculate_dpo(payables, cogs):
    return safe_division(payables, cogs) * 365


def calculate_ccc(dio, dso, dpo):
    return dio + dso - dpo


# Example test
if __name__ == "__main__":
    print("\n--- Working Capital Analyzer ---")

    inventory = float(input("Enter Inventory value: "))
    cogs = float(input("Enter COGS value: "))
    receivables = float(input("Enter Accounts Receivable: "))
    revenue = float(input("Enter Revenue: "))
    payables = float(input("Enter Accounts Payable: "))

    dio = calculate_dio(inventory, cogs)
    dso = calculate_dso(receivables, revenue)
    dpo = calculate_dpo(payables, cogs)
    ccc = calculate_ccc(dio, dso, dpo)

    print("\n--- Results ---")
    print(f"DIO: {round(dio, 2)} days")
    print(f"DSO: {round(dso, 2)} days")
    print(f"DPO: {round(dpo, 2)} days")
    print(f"Cash Conversion Cycle: {round(ccc, 2)} days")
