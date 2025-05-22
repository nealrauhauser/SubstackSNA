from .substsna import mkarango

# call me with datetime.datetime.now()
def elkdate(stamp):
    return(stamp.strftime("%a %b %d %X +0000 %Y"))
def is_number(n):
    try:
        float(n)   # Type-casting the string to `float`.
                   # If string is not a valid `float`,
                   # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True