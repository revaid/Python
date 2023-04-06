def menicPismen(vstupnyString):

    novyString = ""

    for char in vstupnyString:
        if char == "a":
            novyString += "e"

        elif char == "i":
            novyString += "x"

        else:
            novyString += char

    return  novyString 

test = "cau jonatan, das si jablko?"
tlac = menicPismen(test)

print(tlac)