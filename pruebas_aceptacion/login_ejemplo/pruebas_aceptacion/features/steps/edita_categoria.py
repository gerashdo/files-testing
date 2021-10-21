from behave import given, when, then
from selenium import webdriver
import time

@given(u'presiono el boton "Save"')
def step_impl(context):
    context.driver.find_element_by_name("_save").click()

@given(u'presiono en la categoria "{text_categoria}", ingreso el nuevo nombre "{text_ingreso}"')
def step_impl(context, text_categoria, text_ingreso):
    context.driver.find_element_by_link_text(text_categoria).click()
    context.driver.find_element_by_id("id_nombre").clear()
    context.driver.find_element_by_id("id_nombre").send_keys(text_ingreso)