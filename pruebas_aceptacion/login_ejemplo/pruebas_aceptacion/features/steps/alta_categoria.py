from behave import given, when, then
from selenium import webdriver
import time

@given(u'presiono el boton Ingresar')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/form/div[3]/input').click()

@given(u'doy click en el boton "{boton_categoria}"')
def step_impl(context, boton_categoria):
    context.driver.find_element_by_link_text(boton_categoria).click()


@given(u'hago click en el boton "{boton_agregar}"')
def step_impl(context, boton_agregar):
    time.sleep(5)
    context.driver.find_element_by_xpath('/html/body/div/div[3]/div/div[1]/div/ul/li/a').click()


@given(u'ingreso el nombre de categoria "{text_ingreso}"')
def step_impl(context, text_ingreso):
    context.driver.find_element_by_id("id_nombre").send_keys(text_ingreso)


@when(u'presiono el boton "{boton_guardar}"')
def step_impl(context, boton_guardar):
    context.driver.find_element_by_name("_save").click()


@then(u'puedo ver la categoria "{text_resultado}" en la lista de categorias')
def step_impl(context, text_resultado):
    results = context.driver.find_element_by_class_name("results")
    assert results.find_element_by_link_text(text_resultado) is not None