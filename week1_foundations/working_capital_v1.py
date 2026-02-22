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
inventory = 500
cogs = 1000
receivables = 300
revenue = 1200
payables = 400

dio = calculate_dio(inventory, cogs)
dso = calculate_dso(receivables, revenue)
dpo = calculate_dpo(payables, cogs)
ccc = calculate_ccc(dio, dso, dpo)

print("\n--- Working Capital Metrics ---")
print(f"DIO: {round(dio, 2)} days")
print(f"DSO: {round(dso, 2)} days")
print(f"DPO: {round(dpo, 2)} days")
print(f"Cash Conversion Cycle: {round(ccc, 2)} days")
