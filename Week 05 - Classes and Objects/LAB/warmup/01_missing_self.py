# Fixed version.
# This was intentionally broken to practise debugging.

class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self, percent):
        return "OVER LIMIT" if percent > self.limit else "OK"


r = Record("R-001", 87.0, 100.0)
print(r.status(95))
