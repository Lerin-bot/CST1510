"""Load records, report their status, and save a results file."""
def check_record(value, limit):
    """Return difference, percentage, and status for a record."""
    difference = value - limit
    percent = value / limit * 100
    status = "OVER LIMIT" if percent >= 100 else "WARNING" if percent >= 90 else "OK"
    return difference, percent, status

def print_report(label, value, limit, difference, percent, status):
    """Print one formatted record report."""
    print("\n" + "=" * 34 + f"\n  RECORD CHECK - {label}\n" + "=" * 34)
    print(f"  Value       : {value:>10.2f}\n  Limit       : {limit:>10.2f}\n  Difference  : {difference:>+10.2f}\n  Percent     : {percent:>10.2f}%\n  Status      : {status}")
    print("=" * 34)

def load_records(path):
    """Read label,value,limit rows, skipping a CSV header if present."""
    records = []
    try:
        with open(path, encoding="utf-8") as source:
            for line in source:
                fields = line.strip().split(",")
                if len(fields) != 3 or fields[0].lower() == "label":
                    continue
                records.append({"label": fields[0], "value": float(fields[1]), "limit": float(fields[2])})
    except FileNotFoundError:
        print(f"Could not find {path}")
    return records

records = load_records("records_sample.txt")
over_count = 0
with open("results.txt", "w", encoding="utf-8") as output:
    for record in records:
        difference, percent, status = check_record(record["value"], record["limit"])
        print_report(record["label"], record["value"], record["limit"], difference, percent, status)
        over_count += status == "OVER LIMIT"
        output.write(f"{record['label']},{status}\n")
print(f"Records over limit: {over_count}")
