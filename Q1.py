# Q1-a
def formataData(data):

    dic = {"Ano": -1, "Mes": -1, "Dia": -1}

    separaData = data.split("/")

    dic["Ano"] = separaData[2]
    dic["Mes"] = separaData[1]
    dic["Dia"] = separaData[0]

    return dic

# b
def ativoBooleano(ativo):

    resp = []
    resp += ativo
    result = resp [:-1]

    print (result)

    if result == "S":
        result = True
        return result

    else:
        result = False
        return result

# c
def listaStrings(string):

    lista = string.split(":")

    return lista

#d
def leiaArquivo(arquivo):
    arquivo.seek(0)
    lista = arquivo.readlines()

    return lista

#e
def main(data,ativo,string,arquivo,listaDicionarios):

    formataData(data)
    ativoBooleano(ativo)
    listaStrings(string)
    leiaArquivo(arquivo)

    arquivo.read()

    print(listaDicionarios)

    arquivo.close()
