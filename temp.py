def celckel(temp):
    f = temp + 273.15
    return f

def celcfar(temp):
    f = (temp * 9 / 5) + 32
    return f

def farcelc(temp):
    f = (temp - 32) * 5 / 9
    return f

def kelcelc(temp):
    f = temp - 273.15
    return f

def farkel(temp):
    f = (temp - 32) * (5 / 9) + 273.15
    return f

def kelfar(temp):
    f = (temp - 273.15) * (9 / 5) + 32
    return f
