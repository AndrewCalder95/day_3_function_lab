def return_10():
    return 10 

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def length_of_string(a):
    return len(a)

def join_string(a, b):
    return f"{a}{b}"

def add_string_as_number(a,b):
    return int(a) + int(b)

months = {
    1 : "January",
    3 : "March",
    4 : "April",
    9 : "September",
    10 : "October"
}

def number_to_full_month_name(a):
    return months[a]

def number_to_short_month_name(a):
    var = (months[a])
    return (var[0:3])