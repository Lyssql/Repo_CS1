import sys
mode = None
if(len(sys.argv) == 3):
    sys.exit(0)
elif(sys.argv[1] == "cypher"):
    mode = "cypher"
elif(sys.argv[1] == "decypher"):
    mode = "decypher"
else:
    print(f"commande non supportée: {sys.argv[1]}")
    sys.exit(0)
key = int(sys.argv[2])
msg = sys.argv[3]

key = key % 26
i = 0
ascii_eq = 0
tab = msg.split
if(mode == "cypher"):
    while i < len(msg):
         ascii_eq = ord(msg[i])
         ascii_eq = ascii_eq + key
         if(ascii_eq > 122):
            ascii_eq = ascii_eq - 97
         tab[i] = chr(ascii_eq)
         i = i + 1

if(mode == "decypher"):
    while i < len(msg):
         ascii_eq = ord(msg[i])
         ascii_eq = ascii_eq - key
         if(ascii_eq < 97):
            ascii_eq = ascii_eq + 26
         tab[i] = chr(ascii_eq)
         i = i + 1
response = ''
j=0
for char in tab:
    response += tab[j]
    j+=1
print(response)