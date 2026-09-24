import glob
import os
import tkinter

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    meio = len(arr) // 2
    esquerda = merge_sort(arr[:meio])
    direita = merge_sort(arr[meio:])

    return merge(esquerda, direita)

def merge(esquerda, direita):
    lista = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            lista.append(esquerda[i])
            i += 1
        else:
            lista.append(direita[j])
            j += 1

    lista.extend(esquerda[i:])
    lista.extend(direita[j:])
    return lista


def dividir_arquivo(nome_arquivo):
    arquivos = []
    numeros = []
    pasta_partes = "partes"
    limite_numero = int(input("Digite o limite de números por arquivo: "))

    os.makedirs(pasta_partes, exist_ok = True)

    with open(nome_arquivo) as arquivo:
        for linha in arquivo:
            numeros.append(int(linha))

            if (len(numeros) == limite_numero):
                numero_arquivo = len(arquivos) + 1
                nome_parte = os.path.join(pasta_partes, f"arquivo_parte_{numero_arquivo:03d}.txt")
                print(f"Arquivo {nome_parte} tem {len(numeros)} números.")

                with open(nome_parte, "w") as parte:
                    parte.write("\n".join(map(str, merge_sort(numeros))))

                arquivos.append(nome_parte)
                numeros = []

    if numeros:
        numero_arquivo = len(arquivos) + 1
        nome_parte = os.path.join(pasta_partes, f"arquivo_parte_{numero_arquivo:03d}.txt")
        print(f"Arquivo {nome_parte} tem {len(numeros)} números.")

        with open(nome_parte, "w") as parte:
            parte.write("\n".join(map(str, merge_sort(numeros))))

        arquivos.append(nome_parte)

    return arquivos

def juntar_arquivos(arquivos):
    partes = [open(nome_arquivo) for nome_arquivo in arquivos]
    numeros = []

    for p in partes:
        linha = p.readline()
        if linha:
            numeros.append(int(linha))
        else:
            numeros.append(None)

    with open("arquivo_ordenado.txt", "w") as arquivo:
        while any(n is not None for n in numeros):
            menor = min(n for n in numeros if n is not None)
            arquivo.write(f"{menor}\n")
            indice = numeros.index(menor)
            linha = partes[indice].readline()
            if linha:
                numeros[indice] = int(linha) 
            else:
                numeros[indice] = None

    for p in partes:
        p.close()

def validar_resultado(arquivo_original, arquivo_final): 
    quantidade_original = 0 
    soma_original = 0 
    soma_quadrados_original = 0

    quantidade_final = 0 
    soma_final = 0 
    soma_quadrados_final = 0 
    ordenado = True 

    with open(arquivo_original) as arquivo:
        for linha in arquivo: 
            numero = int(linha) 
            quantidade_original += 1 
            soma_original += numero 
            soma_quadrados_original += numero ** 2 

    anterior = None 
    with open(arquivo_final) as arquivo: 
        for linha in arquivo: 
            numero = int(linha) 
            quantidade_final += 1 
            soma_final += numero 
            soma_quadrados_final += numero ** 2 


            if (anterior is not None) and (numero < anterior): 
                ordenado = False

            anterior = numero 

    mesma_quantidade = quantidade_original == quantidade_final 
    mesma_soma = soma_original == soma_final 
    mesma_soma_quadrados = soma_quadrados_original == soma_quadrados_final 
    numeros_preservados = ( mesma_quantidade and mesma_soma and mesma_soma_quadrados ) 

    validacao = "\n".join([
        "--- VALIDAÇÃO ---",
        f"Quantidade original: {quantidade_original}",
        f"Quantidade final: {quantidade_final}",
        f"Mesma quantidade: {'SIM' if mesma_quantidade else 'NÃO'}",
        f"Arquivo ordenado corretamente: {'SIM' if ordenado else 'NÃO'}",
        f"Números preservados: {'SIM' if numeros_preservados else 'NÃO'}",
    ])

    return validacao, mesma_quantidade and ordenado and numeros_preservados


if __name__ == "__main__":

    os.makedirs("partes", exist_ok = True)
    for nome_arquivo in glob.glob(os.path.join("partes", "arquivo_parte_*.txt")):
        os.remove(nome_arquivo)

    arquivos = dividir_arquivo("arquivo.txt") 
    juntar_arquivos(arquivos)

    validacao, resultado = validar_resultado("arquivo.txt", "arquivo_ordenado.txt")
    janela = tkinter.Tk()
    janela.title("Validação da ordenação")
    mensagem = f"{validacao}\n\nLista ordenada: {'CONCLUÍDA' if resultado else 'FALHOU'}"
    label = tkinter.Label(janela, text=mensagem, font=("Arial", 16), justify="left", padx=20, pady=20)
    label.pack()
    janela.mainloop()
    