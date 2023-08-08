from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#importe le module By qui contient des méthodes pour localiser les éléments dans une page Web.
from selenium.webdriver.common.by import By
#Ceci importe le module time qui fournit diverses fonctions liées au temps
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#définir des options spécifiques pour le webdriver Chrome.
from selenium.webdriver.chrome.options import Options
#extrarire des données de maniére lisible
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
#L'objet Options est utilisé pour définir les préférences et les options du WebDriver Chrome
def freshservice(email,password,ticket):
    chrome_options = Options()
    #utilise la méthode add_extension de l'objet Options pour ajouter une extension Chrome au WebDriver.
    chrome_options.add_extension('buster.crx')
    #on a ouvrer un navigateur avec une extension
    driver = webdriver.Chrome(chrome_options)
    #le driver a pris le url de la page freshservice
    driver.get("https://isimsf.myfreshworks.com/login?client_id=88601166472310534&redirect_uri=https%3A%2F%2Fisimsf.freshservice.com%2Ffreshid%2Fauthorize_callback%3Fhd%3Disimsf.freshservice.com&account_id=602099877624304383")
    #attendre 5seconde jusqu'a l'apparition du code html
    username = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'username')))
    password = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'password')))

    username.send_keys(email)
    password.send_keys(password)
    login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME,'css-o1ejds')))
    driver.execute_script("arguments[0].scrollIntoView();", login)
    login.click()
    WebDriverWait(driver, 60).until(EC.url_changes(driver.current_url))
    driver.get("https://isimsf.freshservice.com/a/tickets/1?current_tab=details")
    WebDriverWait(driver, 7).until(EC.presence_of_all_elements_located)
    #code source de la page actuel qui contient le ticket
    time.sleep(5)
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    #=========================================================================================priority
    elements_priority = soup.find_all(class_="ember-power-select-selected-item priority-value")
    priority = elements_priority[0].text.strip()
    print("priority :",priority)


    #=========================================================================================contact
    elements_contact = soup.find_all('span',id ='primary_email')
    contact = elements_contact[0].text
    print("contact :",contact.strip())
    #=========================================================================================subject
    elements_subject = soup.find_all('h3',attrs={'class':'subject-text'})
    subject = elements_subject[0].text
    print("subject :",subject.strip())
    #=========================================================================================group
    elements_group = soup.find_all(class_ = "ember-power-select-selected-item has-clear")
    group = elements_group[0].text
    print("group :",group.strip())
    #=========================================================================================description
    elements_description = soup.find_all(class_="view-more-body")
    description = elements_description[0].text
    print("description :",description.strip())
    #=========================================================================================agent
    elements_agent = soup.find_all(class_ = "ember-power-select-selected-item has-clear")
    agent = elements_agent[1].text
    print("Agent :",agent.strip())

    """time.sleep(5)
    driver.get("https://isimsf.freshservice.com/itil/changes/new")"""
    driver.get("https://isimsf.freshservice.com/itil/changes/new")
    #WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located)
    #time.sleep(5)
    #element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,'email_field')))


    #=========================================================================================e-mail
    """element_mail = driver.find_element(By.ID,'itil_change_email')
    element_mail.send_keys(contact)"""

    element_mail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'itil_change_email')))
    element_mail.send_keys(contact)

    #=========================================================================================subject
    """element_subject=driver.find_element(By.ID,"itil_change_subject")
    element_subject.send_keys(subject)"""

    elements_subject = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'itil_change_subject')))
    elements_subject.send_keys(subject)

    #=========================================================================================description
    """
    element_description= driver.find_element(By.XPATH,"/html/body/div[1]/div[10]/div[1]/div/div[2]/div[2]/div[3]/div[1]/div[4]/form/ul/li[11]/div[1]/div[2]/p")
    element_description.send_keys(description)
    
    
    elements_description = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[10]/div[1]/div/div[2]/div[2]/div[3]/div[1]/div[4]/form/ul/li[11]/div[1]/div[2]/p')))
    elements_description.send_keys(contact)
    """
    time.sleep(5000)

