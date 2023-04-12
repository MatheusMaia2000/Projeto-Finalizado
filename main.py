import time


def menu():
  option = "N"
  while option == "N":
    option = input("Você aceita ser minha para sempre S/N ").upper()
    if option != "S":
      print(
        "VAI ACEITAR SIM DESGRAMA S2 TE AMO MEU AMOR VOCÊ E MEU MAIOR PRESENTE"
      )
    else:
      message_count = 0
      while message_count < 3:
        print("Escolha uma mensagem para mim:")
        print("opção 1")
        print("opção 2")
        print("opção 3")
        message_option = input("Opção: ")
        if message_option == "1":
          print(
            "Eu sou grato(a) por você estar ao meu lado. Você é o meu maior presente!"
          )
          message_count += 1
        elif message_option == "2":
          print(
            "Você é a minha inspiração. Tudo o que faço, faço pensando em você."
          )
          message_count += 1
        elif message_option == "3":
          print(
            "Você torna a minha vida mais feliz. Sua presença é o meu maior presente!"
          )
          message_count += 1
        else:
          print("Opção inválida! Por favor, escolha uma opção válida.")
      print("Todas as opções de mensagem foram exibidas. Reiniciando...")
      time.sleep(1)
      print("\n\n           TE AMO, KAMILA! ❤️\n\n")
      time.sleep(1)
      option = "N"


menu()
