#Header

print("=" * 50)
print("")
print(" " * 22, "OLÁ")
print(" " * 4,"SEJA BEM-VINDO(A) AO TEATRO DA EQUIPE 5!")
print("")
print("=" * 50)

#Poltronas Disponiveis
print("""
AS POLTRONAS DISPONIVEIS SÃO:
""")

#poltronas_disponiveis = print("""[A1] [A2] [A3] [A4] [A5]""")

p1 = print("[A1]")
p2 = print("[A2]")
p3 = print("[A3]")
p4 = print("[A4]")
p5 = print("[A5]")
print("")
print("=" * 50)
poltronas_ocupadas = "", "", "", "", ""

#Opções a serem escolhidas

opcao = 0
while opcao != 3:
  opcao = int(input("""
O que você deseja fazer?
  
[1] - Comprar ingresso
[2] - Cancelar reserva
[3] - Sair
  
Escolha uma das opções a cima: """))

  if opcao == 1:
    nome = input("Qual o seu nome? ")
    poltrona_escolhida = input("Qual poltrona você gostaria de reservar? ")
    poltrona_escolhida = poltrona_escolhida.upper()
    if poltrona_escolhida != poltronas_ocupadas:
      poltronas_ocupadas = poltrona_escolhida
      print("")
      print(f"Ótimo {nome}, sua reserva foi feita com sucesso!")
      print(f"""
DETALHES DO INGRESSO:
NOME - {nome}
POLTRONA - {poltrona_escolhida}
      """)
    else:
      print("")
      print("Que pena, a protrona escolhida já foi reservada :(!")
      print("Que tal escolher outra poltrona?")
      print(f"As poltronas já ocupadas são as {poltronas_ocupadas}.")