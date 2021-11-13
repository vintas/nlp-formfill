# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')


def google_search_chromedriver():
    driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.
    driver.get('http://www.google.com/');
    time.sleep(5)  # Let the user actually see something!
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(5)  # Let the user actually see something!
    driver.quit()


def open_patient_visit_slip():
    # driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.
    driver.get('file:///D:/sat/nlp-formfill/patient_visit_slip.html');
    time.sleep(5)  # Let the user actually see something!


def fill_input_box(form_input_text_name, form_input_text_speech_transcribed):
    input_text_element = driver.find_element(by='id', value=form_input_text_name)
    input_text_element.send_keys(form_input_text_speech_transcribed)



def submit_visit_slip():
    submit_button_element = driver.find_element(by='id', value='submit')
    submit_button_element.click()
    time.sleep(5)  # Let the user actually see something!
    driver.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    open_patient_visit_slip()
    form_input_text_name = 'history'
    form_input_text_speech_transcribed = 'Smoker for last 5 years'
    fill_input_box(form_input_text_name, form_input_text_speech_transcribed)
    submit_visit_slip()

