dict1 = {"a": "q","b" : "w","c" : "e","d" : "r","e" : "t","f" : "y","g" : "u","h" : "i","i" : "o","j" : "p","k" : "a","l" : "s","m" : "d","n" : "f","o" : "g","p" : "h","q" : "j","r" : "k","s" : "l","t" : "z","u" : "x","v" : "c","w" : "v","x" : "b","y" : "n","z" : "m",
}

lst = []
decriptedlst = []

valu = input("Enter the value : ")


for char in valu.lower():
    if char in dict1:
        lst.append(dict1.get(char))
print(lst)
tup = tuple(lst)
print(tup)

question = input("do you want to Decript it yeah or Nah : ")

if question.lower() in ["yeah", "yes"]:
    reversedict = {value: key for key, value in dict1.items()}
    
    for cha in lst:
        if cha in reversedict:
            decriptedlst.append(reversedict[cha])
print(decriptedlst)
