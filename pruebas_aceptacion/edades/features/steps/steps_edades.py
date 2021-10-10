from behave import given, when, then
from edades import Edad


@given(u'que ingreso el numero "{edad}"')
def step_impl(context, edad):
    context.edad = int(edad)


@when(u'verifico mi rango de edad')
def step_impl(context):
    edades = Edad()
    context.resultado = edades.calcularEdad(context.edad)


@then(u'puedo ver el mensaje "{esperado}"')
def step_impl(context,esperado):
    assert context.resultado == esperado, f"Se esperaba {esperado} y se obtuvo {context.resultado}"

@given(u'que ingreso la cadena "{edad}"')
def step_impl(context, edad):
    context.edad = edad