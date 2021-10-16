from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://google.com')

caja = driver.find_element_by_name('q')
caja.send_keys('h233444', Keys.ENTER)

try:
    while driver.find_element_by_id('pnnext'):
        div = driver.find_element_by_id('rso')
        titulos = div.find_elements_by_tag_name('h3')
        for titulo in titulos:
            if titulo.text:
                print(titulo.text)

        driver.find_element_by_id('pnnext').click()
except:
    div = driver.find_element_by_id('rso')
    titulos = div.find_elements_by_tag_name('h3')
    for titulo in titulos:
        if titulo.text:
            print(titulo.text)



