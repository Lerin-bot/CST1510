"""Interactive record checker with status decisions and repeated entries."""
count_over = 0
while True:
    label = input("Record label (or quit): ").strip()
    if label.lower() == "quit":
        break
    value = float(input("Value: "))
    limit = float(input("Limit: "))
    percent = value / limit * 100
    difference = value - limit
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    count_over += status == "OVER LIMIT"
    print("\n" + "=" * 34)
    print(f"  RECORD CHECK - {label}")
    print("=" * 34)
    print(f"  Value       : {value:>10.2f}")
    print(f"  Limit       : {limit:>10.2f}")
    print(f"  Difference  : {difference:>+10.2f}")
    print(f"  Percent     : {percent:>10.2f}%")
    print(f"  Status      : {status}")
    print("=" * 34)
print(f"Records over limit: {count_over}")
