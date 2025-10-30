# BIGDATASENAC
diadasemana=int(input('qual dia da semana você quer saber'))
if diadasemana==1:  
    print('domingo')
elif diadasemana==2:
    print('segunda')
elif diadasemana==3:
    print('terça')
elif diadasemana==4:
    print('quarta')
elif diadasemana==5:
    print('quinta') 
elif diadasemana==6:
    print('sexta') 
elif diadasemana==7:
    print('sabado')
else:
    print('numero invalido para essa pergunta')


try:
    diadasemana=int(input('qual dia da semana você quer saber'))
    match diadasemana:
        case 1:
            print('domingo')
        case 2:
            print('segunda')
        case 3:
            print('terça')
        case 4:
            print('quarta')
        case 5:
            print('quinta')
        case 6:
            print('sexta')
        case 7:
            print('sabado')
        case _:
            print('numero invalido')
except:
    print('informação invalida. por favor informe um numero')