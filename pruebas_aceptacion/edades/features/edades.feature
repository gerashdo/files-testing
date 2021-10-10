Característica: Como usuario de edades
                quiero verificar en que rango de edad estoy
                para conocerme mejor

    Escenario: Edad negativa

        Dado que ingreso el numero "-2"
        Cuando verifico mi rango de edad
        Entonces puedo ver el mensaje "No existes"

    Escenario: Edad 0

        Dado que ingreso el numero "0"
        Cuando verifico mi rango de edad
        Entonces puedo ver el mensaje "Eres niño"

    Escenario: Edad 8 años

        Dado que ingreso el numero "8"
        Cuando verifico mi rango de edad
        Entonces puedo ver el mensaje "Eres niño"

    Escenario: Edad 13 años

        Dado que ingreso el numero "13"
        Cuando verifico mi rango de edad
        Entonces puedo ver el mensaje "Eres niño"

    Escenario: Edad 14 años

        Dado que ingreso el numero "14"
        Cuando verifico mi rango de edad
        Entonces puedo ver el mensaje "Eres adolescente"

    Escenario: Edad 17 años

        Dado que ingreso el numero "17"
        Cuando verifico mi rango de edad
        Entonces puedo ver el mensaje "Eres adolescente"

    Escenario: Edad 18 años

        Dado que ingreso el numero "18"
        Cuando verifico mi rango de edad
        Entonces puedo ver el mensaje "Eres adulto"

    Escenario: Edad 65 años

        Dado que ingreso el numero "65"
        Cuando verifico mi rango de edad
        Entonces puedo ver el mensaje "Eres adulto"

    Escenario: Edad 66 años

        Dado que ingreso el numero "66"
        Cuando verifico mi rango de edad
        Entonces puedo ver el mensaje "Eres adulto mayor"

    Escenario: Edad 90 años

        Dado que ingreso el numero "90"
        Cuando verifico mi rango de edad
        Entonces puedo ver el mensaje "Eres adulto mayor"

    Escenario: Edad 121 años

        Dado que ingreso el numero "121"
        Cuando verifico mi rango de edad
        Entonces puedo ver el mensaje "Eres Mumm-Ra"

    Escenario: Edad ingresando una cadena

        Dado que ingreso la cadena "X"
        Cuando verifico mi rango de edad
        Entonces puedo ver el mensaje "Solo numeros"