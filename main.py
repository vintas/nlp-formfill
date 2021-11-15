# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from selenium import webdriver

import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()
#initialize the browser
driver = webdriver.Chrome('chromedriver')


# Function to convert text to speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


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
    time.sleep(10)  # Let the user actually see something!
    driver.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    open_patient_visit_slip()
    form_input_text_name = ''
    while (1):
        # Exception handling to handle
        # exceptions at the runtime
        try:
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)
                # print('here')
                # listens for the user's input
                audio2 = r.listen(source2)

                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                print(MyText)
                if 'history' in MyText.split(' '):
                    form_input_text_name = 'history'
                    form_input_text_speech_transcribed = MyText
                    print("his : " + MyText)  # call function to move to history
                    # fill_input_box(form_input_text_name, form_input_text_speech_transcribed)
                if 'diagnosis' in MyText.split(' ') or 'diagnose'in MyText.split(' '):
                    form_input_text_name = 'diagnosis'
                    form_input_text_speech_transcribed = MyText
                    print("diag : " + MyText)  # call function to move to diag
                    # fill_input_box(form_input_text_name, form_input_text_speech_transcribed)
                if 'prescription' in MyText.split(' ') or 'prescribe' in MyText.split(' '):
                    form_input_text_name = 'prescription'
                    form_input_text_speech_transcribed = MyText
                    print("pres : " + MyText)  # call function to move to pres
                    # fill_input_box(form_input_text_name, form_input_text_speech_transcribed)
                if 'submit' in MyText.split(' ') or 'save' in MyText.split(' '):
                    print("submit")
                    submit_visit_slip()
                    break
                print(form_input_text_name + " : " + MyText)
                if form_input_text_name:
                    fill_input_box(form_input_text_name, MyText)


        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occured")

