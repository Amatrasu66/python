dict1 = {"a": "q","b" : "w","c" : "e","d" : "r","e" : "t","f" : "y","g" : "u","h" : "i","i" : "o","j" : "p","k" : "a","l" : "s","m" : "d","n" : "f","o" : "g","p" : "h","q" : "j","r" : "k","s" : "l","t" : "z","u" : "x","v" : "c","w" : "v","x" : "b","y" : "n","z" : "m",
}

lst = []

valu = input("Enter the value : ")

occurance = True

while occurance:
    for val in dict1:
        if("." in valu):
            occurance = False
        elif(valu == dict1.get(val)):
            lst.append(dict1.get(valu))
    print(lst)
