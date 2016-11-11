def arredondar(num):
    return float ( '%0.2f' %(num))
def transformarByteEmMegaByte(bytes):
    megaBytes = int(bytes)/(1024**2)
    return megaBytes

if __name__ == '__main__':
    arq = open('teste.txt','r')
    texto = arq.readlines()
    lista = []
    for linha in texto:
        name = ""
        byte = ""
        for a in linha:
            if a.isdigit():
                byte += a
            else:
                if not(a == ' ' or ord(a) == 10):
                    name += a
        lista.append(name)
        lista.append(byte)
    arq.close()

    lista[1::2] = [arredondar(transformarByteEmMegaByte(x)) for x in lista[1::2]]
    arqR = open('resposta.txt', 'w')
    texto = []
    var = 0
    texto.append('ACME Inc.                 Uso do espaço em disco pelos usuarios\n')
    texto.append('---------------------------------------------------------------\n')
    texto.append('Nr.\tUsuário\tEspaço Utilizado\t% do uso\n\n')
    for i in range(int((len(lista))/2)):
        texto.append('%d\t' %(i))
        texto.append(lista[var]+'\t')
        texto.append('%0.2f%s\t' %(lista[var+1],' MB') )
        texto.append('%0.2f%s\n' %(arredondar(lista[var+1]*100)/sum(lista[1::2]),'%'))
        var+=2
    texto.append('\n%s %0.2f %s\n' %('Espaço total ocupado:', sum(lista[1::2]), 'MB'))
    texto.append('%s %0.2f %s\n' %('Espaço medio ocupado:', sum(lista[1::2])/len(lista[1::2]), 'MB'))
    arqR.writelines(texto)
    arqR.close()

