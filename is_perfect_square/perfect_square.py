from decimal import Context, Decimal, localcontext
import cmath

def is_perfect_square(num, *, complex=False):
    if complex:
        root = cmath.sqrt(num)
        return root.real.is_integer() and root.imag.is_integer()
    if num >= 0:
        cnt = len(str(num))
        with localcontext(Context(prec=cnt*2)):
            root = Decimal(num).sqrt()
            return int(root) ** 2 == num
    else:
        return False
