import sys
import os

arguments = sys.argv[1:]
if not arguments:
      print("infoma o nome do arquivo de email")
      sys.exit(1)
filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)

clientes= []
for line in open(filepath):
      name, email = line.split(",")

      # TODO: substutir com list comprehension
      clientes.append(line.split(","))

      # TODO: substituir por envio de email
      print(f"enviando email para {email}")
      print()
      print( open(templatepath).read() % {"nome": name,"produto": "caneta", "texto": "escreve muito bem", "link": "amazon.com","quantidade": 1,"preco": 50.5})
      print("-"* 50)
