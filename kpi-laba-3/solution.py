def main():

    condition = True
    previous = 1
    while condition:
        current = (2-previous**3)/5

        if abs(current - previous) < 10**(-5):
            condition = False
            return current

        else: previous = current
