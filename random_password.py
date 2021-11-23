import random
import string

def random_password():
    password = ""
    list_symbols = ["@", "#", "$", "%", "&", "?", "!", "-", "_", "+", "-", "*", "/", "|"]
    list_upper = string.ascii_uppercase
    list_lower = string.ascii_lowercase
    list_numbers = [number for number in range(0, 10)]
    vals = [random.choice(list_symbols), random.choice(list_upper), random.choice(list_lower), random.choice(list_numbers)]
    lenght = random.randrange(4, 12) + len(vals)
    while lenght > 0:
        n_random = random.random()
        if n_random < 0.10:
            vals.append(random.choice(list_symbols))
        elif n_random >= 0.10 and n_random < 0.5:
            vals.append(random.choice(list_upper))
        elif n_random >= 0.5 and n_random < 0.9:
            vals.append(random.choice(list_lower))
        else:
            vals.append(random.choice(list_numbers))
        lenght -= 1

    while len(vals) > 0:
        random_val = random.choice(vals)
        password += str(random.choice(vals))
        vals.remove(random_val)
    return print(password)

random_password()


