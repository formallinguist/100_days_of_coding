currency = lambda x : f"${x:,.2f}"
percent = lambda x : f"{x:,.2f}"

print(currency(99))
print(percent(123456.008999))

print(currency(87))
print(percent(45.9990765))