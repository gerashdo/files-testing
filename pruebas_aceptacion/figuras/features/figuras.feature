Característica: Como usuario de figuras
                quiero calcular el area de distintas figuras
                para pasar la clase

    Escenario: Cuadrado con medida de 5 por lado

        Dado que ingreso el numero "5"
        Cuando hago el calculo del area
        Entonces obtengo de resultado "25"

    Escenario: Cuadrado con medida de 8 por lado

        Dado que ingreso el numero "8"
        Cuando hago el calculo del area
        Entonces obtengo de resultado "64"

    Escenario: Cuadrado con medida de -1 por lado

        Dado que ingreso el numero "-1"
        Cuando hago el calculo del area
        Entonces obtengo de mensaje "Solo numeros positivos"

    Escenario: Cuadrado con medida de x por lado

        Dado que ingreso el caracter "x"
        Cuando hago el calculo del area
        Entonces obtengo de mensaje "Solo numeros"

# Circulo

    Escenario: Circulo con medida de 1 de radio

        Dado que ingreso el numero "1"
        Cuando hago el calculo del area del circulo
        Entonces obtengo de resultado del circulo "3.141592653589793"

    Escenario: Circulo con medida de -1de radio

        Dado que ingreso el numero "-1"
        Cuando hago el calculo del area del circulo
        Entonces obtengo de mensaje "Solo numeros positivos"

    Escenario: Circulo con medida de x de radio

        Dado que ingreso el caracter "x"
        Cuando hago el calculo del area del circulo
        Entonces obtengo de mensaje "Solo numeros"

# Rectangulo

    Escenario: Rectangulo con medida de 1 de base y 10 de altura

        Dado que ingreso la base "1" y la altura "10"
        Cuando hago el calculo del area del rectangulo
        Entonces obtengo de resultado "10"

    Escenario: Rectangulo con medida de -1 de base y 5 de altura

        Dado que ingreso la base "-1" y la altura "5"
        Cuando hago el calculo del area del rectangulo
        Entonces obtengo de mensaje "Solo numeros positivos"

    Escenario: Rectangulo con medida de x de base y 2 de altura

        Dado que ingreso la base como caracter "x" y la altura "2"
        Cuando hago el calculo del area del rectangulo
        Entonces obtengo de mensaje "Solo numeros"

# Triangulo

    Escenario: Triangulo con medida de 2 de base y 5 de altura

        Dado que ingreso la base "2" y la altura "5"
        Cuando hago el calculo del area del triangulo
        Entonces obtengo de resultado "5"

    Escenario: Triangulo con medida de -3 de base y -10 de altura

        Dado que ingreso la base "-3" y la altura "-10"
        Cuando hago el calculo del area del triangulo
        Entonces obtengo de mensaje "Solo numeros positivos"

    Escenario: Triangulo con medida de x de base y 5 de altura

        Dado que ingreso la base como caracter "x" y la altura "5"
        Cuando hago el calculo del area del triangulo
        Entonces obtengo de mensaje "Solo numeros"

# Trapezoide

    Escenario: Trapezoide con medida de 5 de base1, 6 de base2 y 2 de altura

        Dado que ingreso la base1 "5", la base2 "6" y la altura "2"
        Cuando hago el calculo del area del treapezoide
        Entonces obtengo de resultado "11"

    Escenario: Trapezoide con medida de -3 de base1, -10 de base2 y 1 de altura

        Dado que ingreso la base1 "-3", la base2 "-10" y la altura "1"
        Cuando hago el calculo del area del treapezoide
        Entonces obtengo de mensaje "Valores no validos"

    Escenario: Trapezoide con medida de 0 de base1, 15 de base2 y 4 de altura

        Dado que ingreso la base1 "0", la base2 "15" y la altura "4"
        Cuando hago el calculo del area del treapezoide
        Entonces obtengo de mensaje "Valores no validos"

    Escenario: Trapezoide con medida de x de base1, 5 de base2 y x de altura

        Dado que ingreso la base1 como caracter "x", la base2 "5" y la altura como caracter "x"
        Cuando hago el calculo del area del treapezoide
        Entonces obtengo de mensaje "Solo numeros"