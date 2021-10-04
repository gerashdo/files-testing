from behave import given, when, then
from calculadora import Calculadora

@given(u'que ingreso los numeros "{num1}" y "{num2}"')
def step_impl(context, num1, num2):
    context.num1 = int(num1)
    context.num2 = int(num2)


@given(u'que ingreso las entradas "{num1}" y "{num2}"')
def step_impl(context, num1, num2):
    context.num1 = num1
    context.num2 = int(num2)


@when(u'realizo la suma')
def step_impl(context):
    calc = Calculadora()
    context.resultado = calc.suma(context.num1, context.num2)


@then(u'puedo ver el resultado "{esperado}"')
def step_impl(context, esperado):
    assert context.resultado == int(esperado), f'esperado es {esperado} y se obtuvo {context.resultado}'


@then(u'puedo ver el mensaje "{mensaje}"')
def step_impl(context, mensaje):
    assert context.resultado == mensaje, f'esperado es {mensaje} y se obtuvo {context.resultado}'


