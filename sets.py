import datetime
today = datetime.datetime.today()
print(f"{today: %B, %d, %Y}")

pi = 3.14766
num = f"{pi:.3f}"
print(f"hello {num}")

sets = {"hello", 9, True, 1}
sets.clear()
print(sets)