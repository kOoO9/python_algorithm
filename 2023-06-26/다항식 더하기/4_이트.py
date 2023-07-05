def solution(polynomial):
    pp = polynomial.split(' + ')
    x, n = 0, 0
    for p in pp:
        if p == 'x':
            x += 1
        elif p[-1] == 'x':
            x += int(p[:-1])
        else:
            n += int(p)
    if x > 0 and n > 0:
        if x == 1:
            return f"x + {n}"
        return f"{x}x + {n}"
    elif x > 0:
        if x == 1:
            return "x"
        return f"{x}x"
    elif n > 0:
        return f"{n}"
    else:
        return str(0)