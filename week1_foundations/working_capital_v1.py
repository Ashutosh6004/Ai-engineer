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

print("DIO:", round(dio, 2))
print("DSO:", round(dso, 2))
print("DPO:", round(dpo, 2))
print("CCC:", round(ccc, 2))
