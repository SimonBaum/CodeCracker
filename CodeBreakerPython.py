# program to solve vierre chiffre

ausgabe = ""

print("Enter password length:")
pw_length = input()

print("Enter file path:")
path = input()

with open(path, "r", encoding='utf-8') as f:
    text = f.readlines()

for x in text:
    ausgabe += x

ausgabe = ''.join(ausgabe.splitlines())
ausgabe = ausgabe.replace("!","")
ausgabe = ausgabe.replace(".","")
ausgabe = ausgabe.replace(";","")
ausgabe = ausgabe.replace(",","")
ausgabe = ausgabe.replace("?","")
ausgabe = ausgabe.replace(":","")
ausgabe = ausgabe.replace("–","")
ausgabe = ausgabe.replace("‘","")
ausgabe = ausgabe.replace(" ","")

ze = len(ausgabe)
test = ""

for char in ausgabe:
    i = 0
    if(i % int(pw_length) == 0):
         test = ausgabe[:i] + str("?") + ausgabe[:i+1]
         i += 1

while(i < ze):
    ersetzen = pw_length*i
    i += 1
    ausgabe = ausgabe.replace("?", 
       
print(ausgabe)
