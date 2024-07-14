import django
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.mail import EmailMessage
from django.conf import settings
from dotenv import load_dotenv
from google_forms import settings


def submit_form():
    # Configure Chrome options
    chrome_options = Options()

    # Initialize WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    
    # Open the Google Form
    driver.get("https://forms.gle/WT68aV5UnPajeoSc8")

    # Fill out the form (modify the selectors and input values as needed)
    time.sleep(2)  # Wait for the page to load

    name_field = driver.find_element(By.XPATH, '//div[@class="Xb9hP"]/input[@aria-labelledby="i1"]')
    name_field.send_keys("Rahul Thorat")

    mobileNo_field = driver.find_element(By.XPATH, '//div[@class="Xb9hP"]/input[@aria-labelledby="i9"]')
    mobileNo_field.send_keys("9552775683")

    email_field = driver.find_element(By.XPATH, '//div[@class="Xb9hP"]/input[@aria-labelledby="i5"]')
    email_field.send_keys("thortarahul2604@gmail.com")

    address_field = driver.find_element(By.XPATH, '//div[@class="Pc9Gce Wic03c"]/textarea[@aria-labelledby="i13"]')
    address_field.send_keys("Addrress")

    pincode_field = driver.find_element(By.XPATH, '//div[@class="Xb9hP"]/input[@aria-labelledby="i17"]')
    pincode_field.send_keys("415110")
 
    birthdate_field = driver.find_element(By.XPATH, '//div[@class="Xb9hP"]/input[@aria-labelledby="i25"]')
    birthdate_field.send_keys("26-04-2003")

    gender_field = driver.find_element(By.XPATH, '//div[@class="Xb9hP"]/input[@aria-labelledby="i26"]')
    gender_field.send_keys("thortarahul2604@gmail.com")

    code = driver.find_element(By.XPATH, '//div[@class="M4DNQ"]//span[@class="M7eMe"]/b').text
    code_field = driver.find_element(By.XPATH, '//div[@class="Xb9hP"]/input[@aria-labelledby="i30"]')
    code_field.send_keys(code)

    # Submit the form
    submit_button = driver.find_element(By.XPATH, '//span[@class="NPEfkd RveJvd snByac" and text()="Submit"]')
    submit_button.click()
    
    # Capture screenshot
    time.sleep(2)  # Wait for the confirmation page to load
    screenshot_path = 'confirmation_screenshot.png'
    driver.save_screenshot(screenshot_path)
    
    # Close the browser
    driver.quit()
    
    return screenshot_path

def send_email(screenshot_path):
    subject = 'Python (Selenium) Assignment - Rahul Thorat'
    body = 'Please find attached the screenshot of the confirmation page.'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = ['sender@gmail.com'] # Replace with sender Mail
    email = EmailMessage(subject, body, from_email, to_email, cc=cc_email)
    email.attach_file(screenshot_path)
    email.send()

if __name__ == "__main__":

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'google_forms.settings')
    django.setup()
    
    screenshot_path = submit_form()
    send_email(screenshot_path)
