def main():
    previous = 1
    while True:
        current = (2-previous**3)/5
        if abs(current - previous) < 10**(-5):
            return current
        else: previous = current
# executing main() function
if __name__ == '__main__':
    main()
