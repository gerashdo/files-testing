Característica: Como usuario del sistema
                quiero registrar una categoria
                para llevar el control de mi inventario

    Escenario: Datos de alta correctos para la categoria
        Dado que ingreso al sistema con la direccion "http://192.168.33.10:8000/"
        Y me dirijo a la pagina de inicio de sesión "admin"
        Y capturo el usuario "admin" y la contraseña "admin"
        Y presiono el boton Ingresar
        Y doy click en el boton "Categorias"
        Y hago click en el boton "Add categoria"
        Y ingreso el nombre de categoria "nueva categoria"
        Cuando presiono el boton "Save"
        Entonces puedo ver la categoria "nueva categoria" en la lista de categorias