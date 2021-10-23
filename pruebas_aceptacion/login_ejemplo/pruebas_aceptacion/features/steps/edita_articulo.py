from behave import given
import time

@given(u'edito el nombre del articulo "{nombre_articulo}", descripcion "{descripcion_articulo}", categoria "{categoria_articulo}", imagen "{imagen_articulo}"')
def step_impl(context, nombre_articulo, descripcion_articulo, categoria_articulo, imagen_articulo):
    context.driver.find_element_by_id("id_nombre").clear()
    context.driver.find_element_by_id("id_nombre").send_keys(nombre_articulo)
    
    context.driver.find_element_by_id("id_descripcion").clear()
    context.driver.find_element_by_id("id_descripcion").send_keys(descripcion_articulo)
    
    context.driver.find_element_by_id("id_categoria").send_keys(categoria_articulo)
    
    context.driver.find_element_by_id("id_foto").clear()
    context.driver.find_element_by_id("id_foto").send_keys(imagen_articulo)
    