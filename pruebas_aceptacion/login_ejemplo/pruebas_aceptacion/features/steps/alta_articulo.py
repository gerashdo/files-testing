from behave import given, when, then


@given(u'ingreso el nombre del articulo "{nombre_articulo}", descripcion "{descripcion_articulo}", categoria "{categoria_articulo}", imagen "{imagen_articulo}"')
def step_impl(context, nombre_articulo, descripcion_articulo, categoria_articulo, imagen_articulo):
    context.driver.find_element_by_id("id_nombre").send_keys(nombre_articulo)
    context.driver.find_element_by_id("id_descripcion").send_keys(descripcion_articulo)
    context.driver.find_element_by_id("id_categoria").send_keys(categoria_articulo)
    context.driver.find_element_by_id("id_foto").send_keys(imagen_articulo)


@then(u'puedo ver el articulo "{nombre_articulo}" en la lista de articulos')
def step_impl(context, nombre_articulo):
    results = context.driver.find_element_by_id("result_list")
    try:
        categoria = results.find_element_by_link_text(nombre_articulo)
    except:
        categoria = None
        
    assert categoria is not None