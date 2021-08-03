

class reloj:
    def solution(self, S, T):

        print('S: ',S)
        print('T: ',T)
        
        x = S.split(':')
        y = T.split(':')

        print('x: ',x)
        print('y: ',y)

        interesting=0
        horaInicial = int(x[0]+x[1]+x[2])
        horaFinal = int(y[0]+y[1]+y[2])

        print('horaInicial: ',horaInicial)
        print('horaFinal: ', horaFinal)

        if horaInicial >= 0 and horaFinal >= horaInicial and horaFinal <=235959: 
            print('x[0]: ', x[0]) #hora inicial
            print('x[1]: ', x[1]) #minuto inicial
            print('x[2]: ', x[2]) #segundo inicial

            print('y[0]: ', y[0]) #hora final
            print('y[1]: ', y[1]) #minuto final
            print('y[2]: ', y[2]) #segundo final

            for h in range(int(x[0]), 24): #rango de horas 24

                if int(str(h)) >= int(x[0]) and int(str(h)) <= int(y[0]): #hora >= a horaInicial y hora <= horaFinal

                    for m in range(int(x[1]), 60): #rango de minutos 60

                        if int(str(m)) >= int(x[1]) and int(str(m)) <= int(y[1]): #minuto >= a minutoInicial y minuto <= minutoFinal
                        
                            for s in range(int(x[2]), 60): #rango de segundos 60
                            
                                if int(str(s)) >= int(x[2]) and int(str(s)) <= int(y[2]): #segundo >= a segundoInicial y segundo <= segundoFinal
                                    
                                    formatted = str(h).zfill(2) + str(m).zfill(2) + str(s).zfill(2) #arma la hora
                                    print('formatted: ', formatted)
                                    print('len: ', len(set(formatted)))
                                    if(len(set(formatted)))==2 or len(set(formatted))==1: #digitos con 1 o 2
                                        interesting+=1
        print('interesante: ', interesting)
       

reloj = reloj()
reloj.solution('00:00:12', '00:00:59')