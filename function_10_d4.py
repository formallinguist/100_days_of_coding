def currency(n, w=0):
    s = f"${n:,.2f}"
    return s.rjust(w)


def percent(n, w=0):
    s = f"{n:.1%}"
    return s.rjust(w)

print(currency(999))
print(percent(1234.9899))