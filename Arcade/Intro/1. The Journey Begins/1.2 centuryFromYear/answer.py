def centuryFromYear(year):
    return year // 100 +  (1 if year % 100 else 0)

def centuryFromYear(year):
    return (year - 1) // 100 + 1

def centuryFromYear(year):
    return (year + 99) // 100

def centuryFromYear(year):
    return year // 100 +  bool(year % 100)