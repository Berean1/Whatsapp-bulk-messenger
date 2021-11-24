# Import all necessary libraries
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException, NoAlertPresentException
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.parse import quote
from sys import platform
import pandas

# read the contacts from CSV file and save them in a list
contacts = pandas.read_csv("Contacts.csv")
numbers = ["+"+str(number) for number in contacts["Number"].to_list()]

# Check if the PC is windows and assign the path for google chrome
options = Options()
if platform == "win32":
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Read the message txt file and save the text contained in message
with open("message.txt", "r") as message_file:
    message = message_file.read()

total_number = len(numbers)

print(f'\n We found  { str(total_number) } numbers in the file')

delay = 30
chrome_driver_path = "C:/Development/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
print('\n Once your browser opens up sign in to web whatsapp')
driver.get('https://web.whatsapp.com')
input("\n Press ENTER after login into Whatsapp Web and your chats are visiable	.")


for idx, number in enumerate(numbers):

    if number == "":
        continue
    print('{}/{} => Sending message to {}.'.format((idx+1), total_number, number))
    try:
        url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
        sent = False
        for i in range(3):
            if not sent:
                driver.get(url)
                try:
                    click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.CLASS_NAME, '_4sWnG')))
                except Exception as e:
                    print(f"Something went wrong..\n Failed to send message to: {number}, retry ({i+1}/3)")
                    print("Make sure your phone and computer is connected to the internet.")
                    print("If there is an alert, please dismiss it.")
                    input("Press enter to continue")
                else:
                    sleep(1)
                    click_btn.click()
                    sent=True
                    sleep(3)
                    print('Message sent to: ' + number)
    except Exception as e:
        print('Failed to send message to ' + number + str(e))






