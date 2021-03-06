from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



def login(browser):
    browser.get("https://www.instagram.com/?hl=es")
    time.sleep(1)
    usuario = browser.find_element_by_css_selector("[name='username']")
    contraseña = browser.find_element_by_css_selector("[name='password']")
    boton = browser.find_element_by_css_selector("button")
    usuario.send_keys("#")
    contraseña.send_keys("#")
    boton.click()
    time.sleep(10)
    botonnoguardarinfo = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
    botonnoguardarinfo.click()
    botonnotificacion = browser.find_element_by_xpath ('/html/body/div[4]/div/div/div/div[3]/button[2]')
    botonnotificacion.click()
    
    

def Visit_Tag(browser, url):
    browser.get(url)
    time.sleep(5)
    pictures = browser.find_elements_by_css_selector("div[class='_9AhH0']")

    image_count = 0

    for picture in pictures:
        if image_count >= 2:
         break
        picture.click()
        time.sleep(3)
        corazon = browser.find_element_by_css_selector("[aria-label='Me gusta']")
        corazon.click()
        cerrar = browser.find_element_by_css_selector("[aria-label='Cerrar']")
        cerrar.click()
        image_count += 1
        time.sleep(5)
    else:
        cerrar = browser.find_element_by_css_selector("[aria-label='Cerrar']")
        cerrar.click()
        time.sleep(5)
        continuar = browser.find_element_by_class_name(" _65Bje  coreSpriteRightPaginationArrow")
        continuar.click()
        time.sleep(5)
      

def main():
    browser = webdriver.Chrome()
    login(browser)

    tags = [ 
        
        "astonmartin",
        "nissan",
        "bugatti",
        "audi",
        "porsche",
        "subaru",
        "mazda",
        "lewishamilton",
        "sebastianvettel",
        "fernandoalonso",
        "kimiräikkönen"
        "michaelschumacher",
    ]



    while True:
        for tag in tags:
            Visit_Tag(browser, f"https://www.instagram.com/explore/tags/{tag}")
        time.sleep(3600)

main()



