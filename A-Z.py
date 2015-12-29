f = open('Input.txt','r')
o = open('Output.txt','w')
for line in f:
    string = ""
    for char in line:
        if char.isalpha() == True:
            if char.lower() == char:
                string += char.upper()
            else:
                string += char.lower()
        else:
            string += char
    o.write(string)
