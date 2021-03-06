from selenium.webdriver import Chrome
from ipdb import spost_mortem

def before_all(context):
    context.browser = Chrome()

def after_step(context, step):
    if step.status == 'failed':
        spost_mortem(step.exc_traceback)

def after_all(context):
    context.browser.quit()
