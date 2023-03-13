
from selenium import webdriver
import time

# Start the WebDriver
browser = webdriver.Chrome('/path/to/chromedriver')

# Open the YouTube live stream page
browser.get('https://www.youtube.com/watch?v=VIDEO_ID')

while True:
    # Type "spam"
    chat_box = browser.find_element_by_xpath('//*[@id="chat-input"]')
    chat_box.send_keys('puan')
    chat_box.submit()
    
    # Wait for 5 minutes
    time.sleep(300)
