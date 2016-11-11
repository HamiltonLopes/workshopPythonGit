if __name__ == '__main__':
    arq = open('teste.txt','w')
    texto = """alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125"""

    arq.write(texto)
    arq.close()