Característica: Como usuario del sistema
                quiero editar un articulo
                para mantener sus caracteristicas actualizadas

    Escenario: Edicion correcta
        Dado que ingreso al sistema con la direccion "http://192.168.33.10:8000/"
        Y me dirijo a la pagina de inicio de sesión "admin"
        Y capturo el usuario "admin" y la contraseña "admin"
        Y presiono el boton Ingresar
        Y doy click en el boton "Articulos"
        Y hago click en el boton "Add articulo"
        Y ingreso el nombre del articulo "nuevo articulo 3", descripcion "nueva descripcion", categoria "categoria 1", imagen "D:\\Programacion\\vagrant\\code\\testing\\pruebas_aceptacion\\Miniatura_Plataforma_1.jpg"
        Y presiono el boton "Save"
        Y presiono en el articulo "nuevo articulo 3"
        Y edito el nombre del articulo "articulo editado", descripcion "descripcion editada", categoria "categoria 2", imagen "D:\\Programacion\\vagrant\\code\\testing\\pruebas_aceptacion\\Miniatura_Plataforma_3.jpg"
        Cuando presiono el boton "Save"
        Entonces puedo ver el articulo "articulo editado" en la lista de articulos