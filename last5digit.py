def getLastDigit(inp, l=5):
    if inp > 9999 :
        return int(str(inp)[-5:])
    else :
        return inp

print(getLastDigit(12345678901247))
print(getLastDigit(123))