Característica: Como usuario del sistema
                quiero iniciar sesión
                para realizar mis tareas diarias dentro de la aplicacion

    Escenario: Usuario y contraseña correctos
        Dado que ingreso al sistema con la direccion "http://192.168.33.10:8000/"
        Y me dirijo a la pagina de inicio de sesión "admin"
        Y capturo el usuario "admin" y la contraseña "admin"
        Cuando presiono el boton Ingresar
        Entonces puedo ver el mensaje "WELCOME, ADMIN."

    Escenario: Usuario y contraseña incorrectos
        Dado que ingreso al sistema con la direccion "http://192.168.33.10:8000/"
        Y me dirijo a la pagina de inicio de sesión "admin"
        Y capturo el usuario "admin" y la contraseña "admin123"
        Cuando presiono el boton Ingresar
        Entonces puedo ver el mensaje de error "Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive."