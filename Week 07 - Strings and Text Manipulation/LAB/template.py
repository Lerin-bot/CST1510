"""Clean, parse, and report on deliberately messy server records."""
def parse_line(raw_line):
    """Normalize a server record and convert its numeric fields."""
    hostname_part, rest = raw_line.strip().split(",", 1)
    record = {"hostname": hostname_part.strip().lower()}
    for field in rest.split(","):
        key, value = field.split("=", 1)
        key, value = key.strip().lower(), value.strip()
        record[key] = float(value) if key in {"used", "total"} else value
    return record

def status_of(record):
    """Return status for the server's used and total capacity."""
    percent = record["used"] / record["total"] * 100
    return "OVER LIMIT" if percent >= 100 else "WARNING" if percent >= 90 else "OK"

raw_records = [
    "  Srv-01 , used=87 , total=100  ",
    "SRV-02,USED=120,TOTAL=100",
    " srv-03, used = 45, total = 100 ",
    "Srv-04,USED=93, total=100",
    "  SRV-05 , used=60 , TOTAL=100",
]
with open("messy_records.txt", "w", encoding="utf-8") as output:
    output.write("\n".join(raw_records) + "\n")
parsed_records = []
with open("messy_records.txt", encoding="utf-8") as source:
    for line in source:
        record = parse_line(line)
        parsed_records.append(record)
        print(record, status_of(record))
flagged = sum(status_of(record) != "OK" for record in parsed_records)
print(f"Records: {len(parsed_records)}; flagged: {flagged}")
