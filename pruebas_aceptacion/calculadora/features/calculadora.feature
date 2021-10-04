Característica: Como usuario de la calculadora 
                quiero hacer operar con dos numeros
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

    Escenario: Solo acepte numeros enteros

        Dado que ingreso "4.5" y "-1" 
        Cuando realizo la suma 
        Entonces puedo ver el mensaje "Solo numeros enteros"

# Resta

    Escenario: Restar quince menos tres

        Dado que ingreso los numeros "15" y "3" 
        Cuando realizo la resta 
        Entonces puedo ver el resultado "12"

    Escenario: Solo acepte numeros positivos

        Dado que ingreso los numeros "-5" y "10" 
        Cuando realizo la resta 
        Entonces puedo ver el mensaje "Solo numeros positivos"

    Escenario: Solo acepte numeros enteros

        Dado que ingreso "4.5" y "-1" 
        Cuando realizo la resta 
        Entonces puedo ver el mensaje "Solo numeros enteros"

    Escenario: Solo acepte numeros, no letras

        Dado que ingreso las entradas "x" y "10" 
        Cuando realizo la resta 
        Entonces puedo ver el mensaje "Solo numeros"

# Multiplicacion

    Escenario: Multiplicar seis por nueve

        Dado que ingreso los numeros "6" y "9" 
        Cuando realizo la multiplicacion 
        Entonces puedo ver el resultado "54"

    Escenario: Multiplicar menos diez por tres

        Dado que ingreso los numeros "-10" y "3" 
        Cuando realizo la multiplicacion 
        Entonces puedo ver el resultado "-30"

    Escenario: Solo acepte numeros enteros

        Dado que ingreso "4.5" y "-1" 
        Cuando realizo la multiplicacion 
        Entonces puedo ver el mensaje "Solo numeros enteros"

    Escenario: Solo acepte numeros, no letras

        Dado que ingreso las entradas "x" y "10" 
        Cuando realizo la multiplicacion 
        Entonces puedo ver el mensaje "Solo numeros"

# Division

    Escenario: Dividir cero entre cero

        Dado que ingreso los numeros "0" y "0" 
        Cuando realizo la division 
        Entonces puedo ver el mensaje "Indefinido"

    Escenario: Dividir cero entre uno

        Dado que ingreso los numeros "0" y "1" 
        Cuando realizo la division 
        Entonces puedo ver el resultado "0"

    Escenario: Dividir uno entre cero

        Dado que ingreso los numeros "1" y "0" 
        Cuando realizo la division 
        Entonces puedo ver el mensaje "Indefinido"

    Escenario: Dividir menos treinta entre menos tres

        Dado que ingreso los numeros "-30" y "-3" 
        Cuando realizo la division 
        Entonces puedo ver el resultado "10"
    
    Escenario: Dividir treinta entre menos tres

        Dado que ingreso los numeros "30" y "-3" 
        Cuando realizo la division 
        Entonces puedo ver el resultado "-10"

    Escenario: Solo acepte numeros enteros

        Dado que ingreso "5.5" y "-1" 
        Cuando realizo la division 
        Entonces puedo ver el mensaje "Solo numeros enteros"

    Escenario: Solo acepte numeros, no letras

        Dado que ingreso las entradas "x" y "10" 
        Cuando realizo la division 
        Entonces puedo ver el mensaje "Solo numeros"

# Potencia

    Escenario: Potenicar cero a la cero

        Dado que ingreso los numeros "0" y "0" 
        Cuando realizo la potencia 
        Entonces puedo ver el mensaje "Indefinido"

    Escenario: Potenicar cero a la cinco

        Dado que ingreso los numeros "0" y "5" 
        Cuando realizo la potencia 
        Entonces puedo ver el resultado "0"

    Escenario: Potenicar once a la cero

        Dado que ingreso los numeros "11" y "0" 
        Cuando realizo la potencia 
        Entonces puedo ver el resultado "1"

    Escenario: Potenicar cuatro a la cinco

        Dado que ingreso los numeros "4" y "5" 
        Cuando realizo la potencia 
        Entonces puedo ver el resultado "1024"

    Escenario: Potenciar menos dos a la menos dos

        Dado que ingreso los numeros "-2" y "-2" 
        Cuando realizo la potencia 
        Entonces puedo ver el resultado de "0.25"

    Escenario: Potenciar menos dos a la dos

        Dado que ingreso los numeros "-2" y "2" 
        Cuando realizo la potencia 
        Entonces puedo ver el resultado "4"

    Escenario: Potenciar dos punto cinco a la dos

        Dado que ingreso "2.5" y "2" 
        Cuando realizo la potencia 
        Entonces puedo ver el resultado de "6.25"

    Escenario: Solo acepte numeros, no letras
        Dado que ingreso las entradas "x" y "10" 
        Cuando realizo la potencia 
        Entonces puedo ver el mensaje "Solo numeros"