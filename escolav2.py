"""
Exibe rrelatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por salas que frequentam
cada uma das atividades
"""

__version__ = "0.1.1"


sala1 = ["Erick","Maia","Gustavo","Manuel","Sofia","Joana"]

sala2 = ["Joao", "Antonio","Carlos","Maria","Isola"]

aula_ingles = ["Erick","Maia","Joana","Carlos","Antonio"]
aula_musica = ["Erick","Carlos","Maria"]
aula_danca = ["Gustavo","Sofia","Joana","Antonio"]

atividades = [("inglês", aula_ingles),
              ("musica", aula_musica),
              ("dança",aula_danca)]

for nome_atividade, atividade in atividades:

    ativadade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2) & set(atividade)


    print(f"A {nome_atividade} sala1",ativadade_sala1)
    print(f"A {nome_atividade} sala2",atividade_sala2)
    print("-" * 40)