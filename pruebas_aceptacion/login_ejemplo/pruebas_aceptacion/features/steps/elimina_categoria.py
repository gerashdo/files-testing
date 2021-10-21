from behave import given, when, then
from selenium import webdriver
import time

@given(u'presiono en la categoria "{text_categoria}"')
def step_impl(context, text_categoria):
    context.driver.find_element_by_link_text(text_categoria).click()
    time.sleep(2)


@given(u'presiono el boton eliminar')
def step_impl(context):
    context.driver.find_element_by_link_text('Delete').click()

@when(u'presiono el boton si, estoy seguro')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div/div[3]/div/div[1]/form/div/input[2]').click()

@then(u'no puedo ver la categoria "{text_resultado}" en la lista de categorias')
def step_impl(context, text_resultado):
    results = context.driver.find_element_by_id("result_list")
    try:
        categoria = results.find_element_by_link_text(text_resultado)
    except:
        categoria = None

    assert categoria is None