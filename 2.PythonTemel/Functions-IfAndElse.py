def summation(a: float, b: float) -> float:
    return a+b


def extraction(a: float, b: float) -> float:
    return a-b


def do_operation(a: float, b: float, operation_type: str) -> float:
    if operation_type == "summation":
        return summation(a,b)
    elif operation_type == "extraction":
        return extraction(a,b)
    else:
        print("Unsupported operation.")


x = 3.0
y = 1.4
print(f" Result: {do_operation(x,y,'summation')} ")
print(f" Result: {do_operation(x,y,'extraction')} ")
