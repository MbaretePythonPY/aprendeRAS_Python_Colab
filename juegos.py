def ahorcado(pwd=d['img']+"palabras.txt"):
    import random
    vidas='******'
    letrasCantadas=''
    file=open(pwd,'r')
    secretos=[line[:-1] for line in file]
    file.close()
    secreto=secretos[random.randrange(0,len(secretos))].upper()
    letra_inicio=random.randrange(0,len(secreto))
    palabra='_ '*len(secreto)
    letra=secreto[letra_inicio]
    while True:
        if (letra in secreto) and (letra not in letrasCantadas):
            letrasCantadas+=letra
            for x in range(len(secreto)):
                if  secreto[x]==letra:
                    palabra=palabra[:2*x]+letra[0]+palabra[2*x+1:]
        elif letra in letrasCantadas:
            print("La letra '"+letra+"', ya fue Cantada...")
            vidas=vidas[:-1]
        else:
            letrasCantadas+=letra
            vidas=vidas[:-1]
        print('\n\nPalabra Secreta:    '+palabra)
        print('Vidas:  '+vidas+', te quedan '+str(len(vidas))+' vidas.')
        print('Letras Cantadas:  '+letrasCantadas)
        if vidas:
            if [l for l in secreto if l not in letrasCantadas]:
                letra=input('Siguiente Letra: <<< ')[0].upper()
            else:
                if input("Muchas Felicidades Lograste Descubrir la palabra secreta "+secreto.upper()+". \n¿Si queres volver a jugar ingresa cualquier letra, sino es asi presiona enter? :<<<"):
                    secreto=secretos[random.randrange(0,len(secretos))]
                    letra_inicio=random.randrange(0,len(secreto))
                    palabra='_ '*len(secreto)
                    letra=secreto[letra_inicio]
                    letrasCantadas=''
                    vidas='******'
                else:
                    break
        else:
            print("Te quedaste sin vidas JAJAJA. \nLa palabra Secreta es: "+secreto)
            break