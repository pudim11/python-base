email_tmpl = """
  olá, %(nome)s
 
  tem interesse em comprar %(produto)s?
 
  este produto é ótimo para resolver
  %(texto)s
 
  Clieque agora em %(link)s
 
  Apenas %(quantidade)d disponeiveis!
 
  Preço promocional %(preco).2f
  """
    
clientes = ["Maria", "João", "Moisés"]
for cliente in clientes:
      print(email_tmpl % {"nome": cliente,"produto": caneta, "texto": "escreve muito bem",
                          "link": "amazon.com","quantidade": 1,"preco": 50;5})