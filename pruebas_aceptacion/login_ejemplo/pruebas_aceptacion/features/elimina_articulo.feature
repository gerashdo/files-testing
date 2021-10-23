Característica: Como usuario del sistema
                quiero eliminar un articulo
                para no tenerlo mas en cuenta

    Escenario: Eliminacion correcta
        Dado que ingreso al sistema con la direccion "http://192.168.33.10:8000/"
        Y me dirijo a la pagina de inicio de sesión "admin"
        Y capturo el usuario "admin" y la contraseña "admin"
        Y presiono el boton Ingresar
        Y doy click en el boton "Articulos"
        Y hago click en el boton "Add articulo"
        Y ingreso el nombre del articulo "nuevo articulo 2", descripcion "nueva descripcion", categoria "categoria 1", imagen "D:\\Programacion\\vagrant\\code\\testing\\pruebas_aceptacion\\Miniatura_Plataforma_1.jpg"
        Y presiono el boton "Save"
        Y presiono en el articulo "nuevo articulo 2"
        Y presiono el boton eliminar
        Cuando presiono el boton si, estoy seguro
        Entonces no puedo ver el articulo "nuevo articulo 2" en la lista de articulos