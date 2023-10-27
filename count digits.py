n = int(raw_input("What is n? "))
def count(n):
    if n < 10:
        return 1
    else:
        return 1 + count(n/10)