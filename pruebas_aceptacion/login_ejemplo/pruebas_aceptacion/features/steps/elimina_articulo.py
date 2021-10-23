from behave import given, then

@given(u'presiono en el articulo "{articulo}"')
def step_impl(context, articulo):
    results = context.driver.find_element_by_id("result_list")
    results.find_element_by_link_text(articulo).click()
    

@then(u'no puedo ver el articulo "{articulo}" en la lista de articulos')
def step_impl(context, articulo):
    results = context.driver.find_element_by_id("result_list")
    try:
        categoria = results.find_element_by_link_text(articulo)
    except:
        categoria = None
        
    assert categoria is None