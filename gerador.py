import random # é o que contém as funções para gerar numeros aleatorios
import string # é o que importa as constantes 



def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha
    



def salvar_senha(senha):
    with open("senha_gerada.txt","a") as arquivo:
        arquivo.write(senha + "\n")
    print("Senha Salva em 'senha_gerada.txt'com sucesso")


def menu():
    print("---Gerador de Senhas---")
    tamanho = (int(input("Digite o tamanho da senha: ")))
    senha = gerar_senha(tamanho)
    print(f"\nSua senha gerada foi: {senha}\n")

    opcao = input("Deseja salvar essa senha em um arquivo txt? (s/n) ").lower()
    if opcao == "s":
        salvar_senha(senha)
    else:
        print("Senha não salva")




menu()