#coding:utf-8
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
        value, byte = "", ""
        for a in linha:
            if a.isdigit():
                byte += a
            else:
                if not(a == ' ' or ord(a) == 10):
                    value += a
        lista.append(value)
        lista.append(byte)
    arq.close()

    lista[1::2] = [arredondar(transformarByteEmMegaByte(x)) for x in lista[1::2]]
    arqR = open('resposta.txt', 'w')
    texto = []
    texto.append('ACME Inc.                 Uso do espaço em disco pelos usuarios\n')
    texto.append('---------------------------------------------------------------\n')
    texto.append('%-5s\t%-15s\t%-8s\t%8s\n\n' %('Nr.','Usuário','Espaço Utilizado','% do uso'))

    for i, value in enumerate(lista):
        if i%2 == 0:
            texto.append('%-5d\t' % (int(i/2)+1))
            texto.append('%-15s\t' %value)
        else:
            texto.append('%8.2f%s\t' % (value, ' MB'))
            texto.append('%15.2f%s\n' % ((value * 100) / sum(lista[1::2]), '%'))

    texto.append('\n%s %0.2f %s\n' %('Espaço total ocupado:', sum(lista[1::2]), 'MB'))
    texto.append('%s %0.2f %s\n' %('Espaço medio ocupado:', sum(lista[1::2])/len(lista[1::2]), 'MB'))
    arqR.writelines(texto)
    arqR.close()
