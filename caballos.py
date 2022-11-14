#diseñe un algoritmo que permita calcular cuántos posibles movimientos válidos puede rea- lizar la ficha del caballo, recibiendo como entrada la cantidad de movimientos a realizar desde el inicio, partiendo de todos los números. Por ejemplo, como mostramos anteriormente si la cantidad de movimientos es uno, la cantidad de movimientos válidos son veinte. Pero si la cantidad de mo- vimientos son dos y se sale desde el 1 se puede ir hasta el 6 y el 8 (un movimiento), a continuación, a partir del 6 hasta el 1, 7 y 0 (dos movimientos de la ficha), luego se sigue desde el 8 hasta el 1 y 3 (para alcanzar los dos movimientos de la ficha). En resumen, se tienen cinco posibles movimientos válidos partiendo desde el 1 (1-6-1, 1-6-7, 1-6-0, 1-8-1 y 1-8-3) a estos se deben sumar todos los movi- mientos que resulten de partir de los demás número. En total la cantidad de posibles movimientos válidos para dos movimientos son 46. Una vez desarrollado el algoritmo complete la siguiente tabla.
#
# Cantidad de movimientos | Cantidad de posibles movimientos
# 1                       | 20
# 2                       | 46
# 3                       | 92
# 4                       | 184
# 5                       | 368
# 6                       | 736
# 7                       | 1472
# 8                       | 2944
# 9                       | 5888
# 10                      | 11776
# 11                      | 23552
# 12                      | 47104
# 13                      | 94208
# 14                      | 188416
# 15                      | 376832
# 16                      | 753664
# 17                      | 1507328
# 18                      | 3014656

# Path: caballos.py
# Compare this snippet from n_reinas.py:
#   if row == n:
#       boards.append([". " * i + "Q " + ". " * (n - 1 - i) for i in possible_board])
#       return


def caballos(n: int) -> int:
    """
    >>> caballos(1)
    20
    >>> caballos(2)
    46
    >>> caballos(3)
    92
    >>> caballos(4)
    184
    >>> caballos(5)
    368
    >>> caballos(6)
    736
    >>> caballos(7)
    1472
    >>> caballos(8)
    2944
    >>> caballos(9)
    5888
    >>> caballos(10)
    11776
    >>> caballos(11)
    23552
    >>> caballos(12)
    47104
    >>> caballos(13)
    94208
    >>> caballos(14)
    188416
    >>> caballos(15)
    376832
    >>> caballos(16)
    753664
    >>> caballos(17)
    1507328
    >>> caballos(18)
    3014656
    """
    return 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()