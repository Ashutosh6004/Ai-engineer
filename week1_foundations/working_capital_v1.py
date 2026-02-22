"""
Working Capital Analyzer Module
Calculates DIO, DSO, DPO, and Cash Conversion Cycle (CCC).

Author: Ashutosh
Purpose: Reusable financial metrics engine for supply chain and AI systems.
"""

def safe_division(numerator: float, denominator: float) -> float:
    """
    Safely divide two numbers.
    Returns 0 if denominator is 0 to avoid ZeroDivisionError.
    """
    if denominator == 0:
        return 0.0
    return numerator / denominator


def calculate_dio(inventory: float, cogs: float) -> float:
    """
    Calculate Days Inventory Outstanding (DIO).

    DIO = (Inventory / COGS) * 365

    Measures how many days inventory remains unsold.
    Higher DIO may indicate slow-moving stock or excess inventory.
    """
    return safe_division(inventory, cogs) * 365


def calculate_dso(receivables: float, revenue: float) -> float:
    """
    Calculate Days Sales Outstanding (DSO).

    DSO = (Accounts Receivable / Revenue) * 365

    Measures how long customers take to pay.
    Higher DSO may signal credit risk or weak collections.
    """
    return safe_division(receivables, revenue) * 365


def calculate_dpo(payables: float, cogs: float) -> float:
    """
    Calculate Days Payables Outstanding (DPO).

    DPO = (Accounts Payable / COGS) * 365

    Measures how long the company takes to pay suppliers.
    Higher DPO improves cash flow but may strain supplier relationships.
    """
    return safe_division(payables, cogs) * 365


def calculate_ccc(dio: float, dso: float, dpo: float) -> float:
    """
    Calculate Cash Conversion Cycle (CCC).

    CCC = DIO + DSO - DPO

    Measures the total time cash is tied up in operations.
    Lower CCC generally indicates better working capital efficiency.
    """
    return dio + dso - dpo


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
