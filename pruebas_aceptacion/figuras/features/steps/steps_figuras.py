from behave import given, when, then
from figuras import Figure


@given(u'que ingreso el numero "{lado}"')
def step_impl(context, lado):
    context.lado = int(lado)

@given(u'que ingreso el caracter "{lado}"')
def step_impl(context, lado):
    context.lado = lado

@when(u'hago el calculo del area')
def step_impl(context):
    figuras = Figure()
    context.resultado = figuras.square(context.lado)


@then(u'obtengo de resultado "{esperado}"')
def step_impl(context, esperado):
    assert context.resultado == int(esperado), f"Se esperaba {esperado} y se obtuvo {context.resultado}"

@then(u'obtengo de mensaje "{esperado}"')
def step_impl(context, esperado):
    assert context.resultado == esperado, f"Se esperaba {esperado} y se obtuvo {context.resultado}"

# Circulo

@when(u'hago el calculo del area del circulo')
def step_impl(context):
    figuras = Figure()
    context.resultado = figuras.circle(context.lado)


@then(u'obtengo de resultado del circulo "{esperado}"')
def step_impl(context, esperado):
    assert context.resultado == float(esperado), f"Se esperaba {esperado} y se obtuvo {context.resultado}"

# Rectangulo

@given(u'que ingreso la base "{base}" y la altura "{altura}"')
def step_impl(context, base, altura):
    context.base = int(base)
    context.altura = int(altura)

@given(u'que ingreso la base como caracter "{base}" y la altura "{altura}"')
def step_impl(context, base, altura):
    context.base = base
    context.altura = int(altura)

@when(u'hago el calculo del area del rectangulo')
def step_impl(context):
    figuras = Figure()
    context.resultado = figuras.rectangle(context.base, context.altura)

# Triangulo

@when(u'hago el calculo del area del triangulo')
def step_impl(context):
    figuras = Figure()
    context.resultado = figuras.triangle(context.base, context.altura)

# Trapezoide

@given(u'que ingreso la base1 "{base1}", la base2 "{base2}" y la altura "{altura}"')
def step_impl(context, base1, base2, altura):
    context.base1 = int(base1)
    context.base2 = int(base2)
    context.altura = int(altura)


@when(u'hago el calculo del area del treapezoide')
def step_impl(context):
    figuras = Figure()
    context.resultado = figuras.trapezoid(context.base1, context.base2, context.altura)

@given(u'que ingreso la base1 como caracter "{base1}", la base2 "{base2}" y la altura como caracter "{altura}"')
def step_impl(context, base1, base2, altura):
    context.base1 = base1
    context.base2 = int(base2)
    context.altura = altura
