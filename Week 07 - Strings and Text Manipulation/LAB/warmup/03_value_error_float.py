# Fixed version.
# This was intentionally broken to practise debugging.

raw_line = "srv-01,used=22,total=100"
hostname_part, rest = raw_line.split(",", 1)

for piece in rest.split(","):
    key, value = piece.split("=")
    print(key, float(value))
