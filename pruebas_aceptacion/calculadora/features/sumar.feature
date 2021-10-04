Característica: Como usuario de la calculadora 
                quiero sumar dos numeros
                para hacer calculos complejos.
    
    Escenario: Sumar dos mas dos

        Dado que ingreso los numeros "2" y "2" 
        Cuando realizo la suma 
        Entonces puedo ver el resultado "4"

    Escenario: Sumar cinco mas diez

        Dado que ingreso los numeros "5" y "10" 
        Cuando realizo la suma 
        Entonces puedo ver el resultado "15"

    Escenario: Solo acepte numeros positivos

        Dado que ingreso los numeros "-5" y "10" 
        Cuando realizo la suma 
        Entonces puedo ver el mensaje "Solo numeros positivos"

    Escenario: Solo acepte numeros, no letras

        Dado que ingreso las entradas "x" y "10" 
        Cuando realizo la suma 
        Entonces puedo ver el mensaje "Solo numeros"