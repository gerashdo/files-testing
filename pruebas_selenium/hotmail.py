from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from datos import contra, correo
# import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=options)

driver.implicitly_wait(10)
driver.get('https://outlook.live.com/')


driver.find_element_by_link_text('Iniciar sesión').click()

driver.find_element_by_name('loginfmt').send_keys(correo)

driver.find_element_by_id('idSIButton9').click()

driver.find_element_by_name('passwd').send_keys(contra)

# Espera y click en siguiente para la contraseña
wait = WebDriverWait(driver, 10)
boton = wait.until(EC.element_to_be_clickable((By.ID, 'idSIButton9')))
boton.click()

# Espera y click en no quedarse logueado
boton = wait.until(EC.element_to_be_clickable((By.ID, 'idBtn_Back')))
boton.click()


# Mails bandeja entrada

divs = driver.find_elements_by_class_name('_24WqHp8mfxSp2QIJMkmSrM')

# Scroll no logrado

# scrollbar = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/div[1]/div[2]/div/div/div/div/div')
# while len(divs) < 100:
#     scrollbar.send_keys(Keys.END)
#     divs = driver.find_elements_by_class_name('_24WqHp8mfxSp2QIJMkmSrM')
#     print(len(divs))

# Imprimir asunto mail

cont = 1
for div in divs:
    if cont >= 101:
        break
    else:
        try:
            print(f"entra")
            titulo = div.find_element_by_tag_name('span').text
            print (f"{cont} {titulo}")
            cont += 1
        except:
            print(f"No encontro")


# Correo no deseado
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div[4]/div').click()

boton = wait.until(EC.element_to_be_clickable((By.NAME, 'Vaciar carpeta')))
boton.click()

boton = wait.until(EC.element_to_be_clickable((By.ID, 'ok-7')))
boton.click()



# Elementos eliminados
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div[7]/div').click()

driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]').click()

boton = wait.until(EC.element_to_be_clickable((By.ID, 'ok-1')))
boton.click()