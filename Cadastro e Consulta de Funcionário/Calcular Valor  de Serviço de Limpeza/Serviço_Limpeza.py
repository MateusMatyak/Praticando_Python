print('Serviços de Limpeza')

# Função metragem da área
def metragem_limpeza():
    print("----------------- MENU 1 de 3 - METRAGEM DE LIMPEZA ----------------")
    print("Qual a metragem(em m²) da área?")
    while True:
        metragem = input("Digite um valor -> ")
        try:
            metragem = int(metragem)
            if not 30 <= metragem < 700:
                print("!!Não aceitamos metragem menor que 30m² e maior que 700m²!!")
            elif 30 <= metragem < 700:
                metragem = int(metragem)
                if 30 <= metragem < 300:
                    valor_metragem = 60 + 0.3 * metragem
                    funcionarios = "É necessário contratar 1 pessoa"
                    print("É necessário contratar 1 pessoa\n")
                else:
                    valor_metragem = 120 + 0.5 * metragem
                    funcionarios = "É necessário contratar 2 pessoas"
                    print("É necessário contratar 2 pessoas!\n")
                return valor_metragem, funcionarios
        except:
            print("!!Campo deve se preenchido com números!!")
 # Função tipo de limpeza
def tipo_limpeza():
    print("------------------- MENU 2 DE 3 - TIPO DE LIMPEZA ------------------")
    print("Qual o tipo de limpeza será feita?"
          "\nB - Limpeza básica. "
          "\nC - Limpeza Completa. ")
    while True:
        tipo = input("Digite um valor -> ")
        try:
            if tipo == "B" or tipo == "b":
                multiplicador = 1.00
                serviço = 'Limpeza Básica'
            elif tipo == "C" or tipo == "c":
                multiplicador = 1.30
                serviço = 'Limpeza Completa'
            return multiplicador, serviço
        except:
            print("!!Opção Inválida!!")
# Função adicional da limpeza
def adicional_limpeza():
    print("------------------- MENU 3 DE 3 - ADICIONAIS ------------------")
    aux = 0
    print("0 - Não desejo mais nada (encerrar)"
          "\n1 - Passar 10 peças de roupas - R$10,00"
          "\n2 - Limpeza de um Forno/Micro-ondas - R$12,00"
          "\n3 - Limpeza de uma Geladeira/Freezer - R$20,00")
    while True:
        adicional = input("Deseja mais algum serviço adicional? -> ")
        try:
            if int(adicional) == 0:
                break
            elif int(adicional) in tipos_adicional or int(adicional) <= 3:
                aux = aux + valor_adicional[int(adicional)]
                print(f"Adicional '{adicional}' Incluído :)")
            elif int(adicional) >= 4:
                print(f"!!A opção '{adicional}' não existe !!")
            else:
                continue
        except:
            print("!!Campo deve se preenchido com números!!")
    return aux
# Tabela adicionais
tipos_adicional = {0: "Não desejo mais nada (encerrar)",
                   1: "Passar 10 peças de roupas - R$10,00",
                   2: "Limpeza de um Forno/Micro-ondas - R$12,00",
                   3: "Limpeza de uma Geladeira/Freezer - R$20,00"}
valor_adicional = [0, 10.00, 12.00, 20.00]
# Soma de valores e resumo
valor, funcionarios = metragem_limpeza()
tipo_limpeza, serviço = tipo_limpeza()
adicionais = adicional_limpeza()
total = (valor * tipo_limpeza) + adicionais
print("------------------- Resumo do Serviço Contratado ------------------")
print(f"Valor Total -> R$ {total:,.2f}")
print(f"Metragem -> R$ {valor:,.2f}")
print(f"Limpeza -> {tipo_limpeza},{serviço}")
print(f"Adicionais -> R$ {adicionais:,.2f}")
print(f"Mão de obra -> {funcionarios}\n")
input("\nPressione Enter Para Sair")

