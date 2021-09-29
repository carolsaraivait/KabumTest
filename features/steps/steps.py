from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from json import loads

@given('que eu esteja na pagina')
def go_to_page(context):
    context.browser.get('https://www.kabum.com.br/')


@when('criar um todo')
def create_todo(context):
    texto_do_step = loads(context.text)
    context.browser.find_element_by_id('input-busca').send_keys(texto_do_step['produto'])
    context.browser.find_element_by_id("input-busca").send_keys(Keys.ENTER)
    
    # import ipdb; 
    
    
@then('o todo deve estar na pilha "{pilha}"')
def check_todo(context, pilha):
    ...
   # assert 'é top' in context.browser.find_element_by_class_name('body_a').text
   # assert 'celuar' in context.browser.find_element_by_class_name('body_a').text