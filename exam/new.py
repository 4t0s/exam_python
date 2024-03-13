from tabulate import tabulate
print(tabulate({"Name": ["Alice", "Bob"],"Age": [24, 19]}, headers="keys"))
print(tabulate({"Name": ["Alice", "Bob"],"Age": [24, 19]}, headers="keys", tablefmt="grid"))