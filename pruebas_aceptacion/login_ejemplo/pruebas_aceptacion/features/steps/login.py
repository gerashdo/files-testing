from behave import given, when, then
from selenium import webdriver
import time

@given(u'que ingreso al sistema con la direccion "{url}"')
def step_impl(context, url):
    context.url = url


@given(u'me dirijo a la pagina de inicio de sesión "{pagina}"')
def step_impl(context, pagina):
    context.driver = webdriver.Chrome()
    context.driver.get(f"{context.url}{pagina}")

@given(u'capturo el usuario "{usuario}" y la contraseña "{contra}"')
def step_impl(context, usuario, contra):
    context.driver.find_element_by_name('username').send_keys(usuario)
    context.driver.find_element_by_name('password').send_keys(contra)

@when(u'presiono el boton Ingresar')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/form/div[3]/input').click()

@then(u'puedo ver el mensaje "{mensaje}"')
def step_impl(context, mensaje):
    respuesta = context.driver.find_element_by_id('user-tools').text
    assert mensaje in respuesta, f"Se esperaba {mensaje} y se obtuvo {respuesta}"

@then(u'puedo ver el mensaje de error "{mensaje}"')
def step_impl(context, mensaje):
    respuesta = context.driver.find_element_by_class_name('errornote').text
    assert mensaje == respuesta, f"Se esperaba {mensaje} y se obtuvo {respuesta}"