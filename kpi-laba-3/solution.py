def main():

    xn_0 = 1

    while True:
        xn = (2-xn_0**3)/5
        if abs(xn - xn_0) < 10**(-5):
            return xn
            break
        else: xn_0 = xn
