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


@given(u'que ingreso "{num1}" y "{num2}"')
def step_impl(context, num1, num2):
    context.num1 = float(num1)
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


# Resta

@when(u'realizo la resta')
def step_impl(context):
    calc = Calculadora()
    context.resultado = calc.resta(context.num1, context.num2)

# Multiplicacion

@when(u'realizo la multiplicacion')
def step_impl(context):
    calc = Calculadora()
    context.resultado = calc.multiplica(context.num1, context.num2)

# Division

@when(u'realizo la division')
def step_impl(context):
    calc = Calculadora()
    context.resultado = calc.divide(context.num1, context.num2)

# Potencia

@when(u'realizo la potencia')
def step_impl(context):
    calc = Calculadora()
    context.resultado = calc.potencia(context.num1, context.num2)


@then(u'puedo ver el resultado de "{esperado}"')
def step_impl(context, esperado):
    assert context.resultado == float(esperado), f"esperado es {esperado} y se obtuvo {context.resultado}"


