#LUCAS MACIEL CARDOSO

valid = str(input("Qual nome do arquivo TXT que você deseja colocar?: "))
arquivo = open(valid + '.txt', 'r')
txt = arquivo.readlines()
z = 0

while z < len(txt):
  txt[z] = txt[z].replace('\n', '')
  txt[z] = txt[z].replace(' ', '')
  z += 1

print("\nSerão realizadas " + txt[0] + " operações: \n")

for x in range(len(txt)):

  if txt[x] == "U":
    conjunto1 = set(txt[x + 1].split(","))
    conjunto2 = set(txt[x + 2].split(","))
    res = conjunto1.union(conjunto2)
    print("União: Conjunto 1 ", conjunto1, ", Conjunto 2 ", conjunto2, ". Resultado: ", res, "\n")
    
  elif txt[x] == "I":
    conjunto1 = set(txt[x + 1].split(","))
    conjunto2 = set(txt[x + 2].split(","))
    res = conjunto1.intersection(conjunto2)
    print("Intersecção: Conjunto 1 ", conjunto1, ", Conjunto 2 ", conjunto2,". Resultado: ", res, "\n")
  
  elif txt[x] == "D":
    conjunto1 = set(txt[x + 1].split(","))
    conjunto2 = set(txt[x + 2].split(","))
    res = conjunto1.difference(conjunto2)
    print("Diferença: Conjunto 1 ", conjunto1, ", Conjunto 2 ", conjunto2,". Resultado: ", res, "\n")
  
  elif txt[x] == "C":
    conjunto1 = txt[x + 1].split(",")
    conjunto2 = txt[x + 2].split(",")
    y = int(0)
    z = int(0)
    res = []
    for y in range(len(conjunto1)):
      for z in range(len(conjunto2)):
        res.append("{" + conjunto1[y] + ", " +  conjunto2[z] + "}")
    conres1 = set(conjunto1)
    conres2 = set(conjunto2)
    print("Produto Cartesiano: Conjunto 1 ", conres1, ", Conjunto 2 ", conres2,". Resultado: ", res)
  x += 1
