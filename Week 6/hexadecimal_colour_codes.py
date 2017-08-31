COLOUR_TO_HEXADECIMAL = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "Beige": "#f5f5dc",
                         "Black": "#000000", "BlanchedAlmond": "#ffebcd", "CadetBlue": "#5f9ea0",
                         "Chocolate": "#d2691e", "BlueViolet": "#8a2be2", "Brown": "#a52a2a", "Burlywood": "#deb887"}

colour = input("Enter a colour: ")
while colour != "":
    if colour in COLOUR_TO_HEXADECIMAL:
        print(colour, "is", COLOUR_TO_HEXADECIMAL[colour])
    else:
        print("Invalid Colour")
    colour = input("Enter a colour: ")

