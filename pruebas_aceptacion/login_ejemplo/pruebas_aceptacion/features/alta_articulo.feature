Característica: Como usuario del sistema del sistema
                quiero dar de alta un articulo
                para llevar el control de mi inventario

    Escenario: Datos de alta correctos
        Dado que ingreso al sistema con la direccion "http://192.168.33.10:8000/"
        Y me dirijo a la pagina de inicio de sesión "admin"
        Y capturo el usuario "admin" y la contraseña "admin"
        Y presiono el boton Ingresar
        Y doy click en el boton "Articulos"
        Y hago click en el boton "Add articulo"
        Y ingreso el nombre del articulo "nuevo articulo", descripcion "nueva descripcion", categoria "categoria 1", imagen "D:\\Programacion\\vagrant\\code\\testing\\pruebas_aceptacion\\Miniatura_Plataforma_1.jpg"
        Cuando presiono el boton "Save"
        Entonces puedo ver el articulo "nuevo articulo" en la lista de articulos