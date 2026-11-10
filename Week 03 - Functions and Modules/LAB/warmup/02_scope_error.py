# Fixed version.
# This was intentionally broken to practise debugging.

def check(value, limit):
    status = "OVER LIMIT" if value > limit else "OK"
    return status

result = check(87, 100)

print(result)
