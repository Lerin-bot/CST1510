"""Interactive record check: input/output, numeric calculations, and formatting."""
label = input("Record label / hostname: ").strip()
value = float(input("Value used / loaded: "))
limit = float(input("Total / expected: "))
difference = limit - value
percent = value / limit * 100
print("\n" + "=" * 34)
print(f"  RECORD CHECK - {label}")
print("=" * 34)
print(f"  Value       : {value:>10.2f}")
print(f"  Total       : {limit:>10.2f}")
print(f"  Difference  : {difference:>+10.2f}")
print(f"  Percent     : {percent:>10.2f}%")
print("=" * 34)
