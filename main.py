#!/bin/python3
import sys

def main():
    min_f = [0, 1]
    max_f = [1, 1]

    n = 0
    try:
        if len(sys.argv) == 2:
            n = float(sys.argv[1].replace(",", "."))
    except ValueError:
        pass

    if not n:
        while True:
            try:
                while not 0 < n < 1:
                    n = float(input(">>> ").replace(",", "."))
                break
            except ValueError:
                pass

    while True:
        try:
            new_f = [min_f[0] + max_f[0], min_f[1] + max_f[1]]
            out_txt = "{{new_f[0]:>5}}/{{new_f[1]:<5}} = {{new_f[0]/new_f[1]:<{0}.3}} | {{n}}".format(len(str(n))+1)
            print()  # {new_f[0]:>5}/{new_f[1]:<5} = {new_f[0]/new_f[1]:<5.3} | {n}")
            if n == new_f[0]/new_f[1]:
                break
            elif n > new_f[0]/new_f[1]:
                min_f = new_f
            else:
                max_f = new_f
            # input("·")
        except KeyboardInterrupt as e:
            break


if __name__ == '__main__':
    main()
