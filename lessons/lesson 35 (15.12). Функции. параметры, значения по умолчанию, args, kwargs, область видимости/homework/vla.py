def format_message(name, text, prefix="", suffix="", tags=None):
    result = ""
    if prefix:
        result += f"{prefix} "
    result += f"{name}, {text}!"
    if suffix:
        result += f" {suffix}"
    if tags is not None:
        result += f" Теги: {tags}"
    return result

def calculate(operation, *args):
    if not args:
        return 0
    
    if operation == "sum":
        total = 0
        for num in args:
            total += num
        return total
    elif operation == "mean":
        total = 0
        for num in args:
            total += num
        return total / len(args)
    elif operation == "max":
        current_max = args[0]
        for num in args[1:]:
            if num > current_max:
                current_max = num
        return current_max
    return None

def update_profile(**kwargs):
    return kwargs

total_energy = 50

def add_energy_v1(amount):
    global total_energy
    total_energy += amount

def add_energy_v2(current_energy, amount):
    return current_energy + amount
