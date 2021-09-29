from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from json import loads
import time

@given('ir para a pagina da Kabum')
def go_to_page(context):
    context.browser.get('https://www.kabum.com.br/')

@when('realizar busca de produto')
def create_todo(context):
    texto_do_step = loads(context.text)
    context.browser.find_element_by_id('input-busca').send_keys(texto_do_step['produto'])
    context.browser.find_element_by_id("input-busca").send_keys(Keys.ENTER)
    time.sleep(5)
    
@then('o produto deve estar no resultado "{produto}"')
def check_todo(context, produto):
    element = context.browser.find_elements_by_class_name('imageCard')[0]
    h2 = element.find_element_by_xpath("//h2")
    assert produto in h2.text

@when('adicionar o produto ao carrinho')
def add_product(context):
    element = context.browser.find_elements_by_class_name('imageCard')[0]
    actionChains = ActionChains(context.browser)
    actionChains.move_to_element(element).perform()
    time.sleep(2)
    element.find_element_by_xpath("//button[text()='COMPRAR']").click()
    time.sleep(5)
    context.browser.find_element_by_xpath("//button[text()='IR PARA O CARRINHO']").click()
    time.sleep(5)

@then('o produto deve estar no carrinho "{produto}"')
def verifica_carrinho(context, produto):
    e = context.browser.find_element_by_xpath("//*[text()='Cartucho de Tinta HP Designjet 711, Magenta - CZ135AB']")
    assert produto in e.text