"""Record checker structured with reusable functions."""
def check(value, limit):
    """Return difference and percentage for one record."""
    return value - limit, value / limit * 100

def status_of(percent):
    """Return the status label for a percentage."""
    if percent >= 100: return "OVER LIMIT"
    if percent >= 90: return "WARNING"
    return "OK"

def print_report(label, value, limit, difference, percent, status):
    """Print a formatted record report."""
    print("\n" + "=" * 34)
    print(f"  RECORD CHECK - {label}")
    print("=" * 34)
    print(f"  Value       : {value:>10.2f}")
    print(f"  Limit       : {limit:>10.2f}")
    print(f"  Difference  : {difference:>+10.2f}")
    print(f"  Percent     : {percent:>10.2f}%")
    print(f"  Status      : {status}")
    print("=" * 34)

label = input("Record label (or quit): ").strip()
while label.lower() != "quit":
    value = float(input("Value: "))
    limit = float(input("Limit: "))
    difference, percent = check(value, limit)
    print_report(label, value, limit, difference, percent, status_of(percent))
    label = input("Record label (or quit): ").strip()
