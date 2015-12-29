f = open("Input.txt","r")
o = open("Output.txt","w")
for line in f:
    string = ""
    for char in line:
        if char == "M":
            string += "m"
        elif char == "m":
            string += "M"
        else:
            string += char
    o.write(string)
