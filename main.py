import os
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

USERNAME = os.getenv('LINKEDIN_USERNAME')
PASSWORD = os.getenv('LINKEDIN_PASSWORD')

if __name__ == '__main__':
    driver = webdriver.Edge()
    url = 'https://www.linkedin.com'

    driver.get(url)
    driver.maximize_window()

    username_input = driver.find_element(by=By.ID, value='session_key')
    password_input = driver.find_element(by=By.ID, value='session_password')
    submit_button = driver.find_element(by=By.XPATH,
                                        value='//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')

    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)

    submit_button.click()
    sleep(3)

    driver.get(
        url + '/search/results/people/?geoUrn=%5B"106057199"%5D&keywords=tech%20recruiter&origin=FACETED_SEARCH'
              '&talksAbout=%5B"techrecruiter"%5D')

    result_container = driver.find_element(by=By.CLASS_NAME, value='search-results-container')
    recruiters_element = driver.find_elements(by=By.CSS_SELECTOR,
                                              value='a.app-aware-link[data-test-app-aware-link]['
                                                    'href^="https://www.linkedin.com/in"]')

    recruiters = []
    for recruiter_element in recruiters_element:
        if recruiter_element.location.get('x') == 440 or (
                len(recruiter_element.text.split('\n')) > 1 and
                'ver perfil' in recruiter_element.text.split('\n')[1].lower()
        ):
            recruiters.append(recruiter_element)

    for recruiter in recruiters:
        recruiter.click()
        more_button = driver.find_element(by=By.XPATH,
                                          value='/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/'
                                                'div[3]/div/div[2]/button')
        more_button.click()

        connect_button = driver.find_element(by=By.XPATH,
                                             value='div[role="button"].artdeco-dropdown__item'
                                                   '.artdeco-dropdown__item--is-dropdown.ember-view.full-width.display-flex'
                                                   '.align-items-center')
        connect_button.click()
        note_button = driver.find_element(by=By.XPATH, value='button[aria-label="Adicionar nota"].artdeco-button'
                                                             '.artdeco-button--muted.artdeco-button--2'
                                                             '.artdeco-button--secondary.ember-view.mr1')

        note_button.click()
        message_area = driver.find_element(by=By.NAME, value='message')
        send_button = driver.find_element(by=By.XPATH, value='button[aria-label="Enviar agora"]#ember538.artdeco-button'
                                                             '.artdeco-button--2.artdeco-button--primary'
                                                             '.artdeco-button--disabled.ember-view.ml1[disabled]')

        message_area.send_keys(
            'Olá, tudo bem? \nSe por acaso ainda estiver contratando, ou conhecer alguém que esteja, pode me indicar? '
            'Estou procurando novas oportunidades.\nObrigado!')

        driver.back()

    sleep(10)
    driver.quit()
