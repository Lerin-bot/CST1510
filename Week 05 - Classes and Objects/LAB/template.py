"""Class based record checking with a class level count."""
class Record:
    """Represent a measured value and its limit."""
    over_limit_count = 0
    def __init__(self, label, value, limit):
        """Initialize a record and count values above their limit."""
        self.label, self.value, self.limit = label, value, limit
        if value > limit:
            Record.over_limit_count += 1
    def percent(self):
        """Return value as a percentage of limit."""
        return self.value / self.limit * 100
    def status(self):
        """Return the status associated with this record's percentage."""
        p = self.percent()
        return "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"

def load_records(path):
    """Load comma separated records as Record objects."""
    with open(path, encoding="utf-8") as source:
        return [Record(label, float(value), float(limit)) for label, value, limit in (line.strip().split(",") for line in source)]

records = load_records("records_sample.txt")
for record in records:
    print("\n" + "=" * 34)
    print(f"  RECORD CHECK - {record.label}")
    print("=" * 34)
    print(f"  Value  : {record.value:.2f}\n  Limit  : {record.limit:.2f}\n  Status : {record.status()}")
    print("=" * 34)
print(f"Records over limit: {Record.over_limit_count} of {len(records)}")
