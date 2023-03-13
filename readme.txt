here's the Python code for a bot that will open any browser and write "!puan" every 5 minutes on a live YouTube stream:

First, we need to install the Selenium library. If you don't have it installed, you can install it with the following command:


pip install selenium


We also need to download the WebDriver that Selenium will use to control the browser. If we're using Chrome, we can download the ChromeDriver. You can download it from this link and save the file on your computer:

https://sites.google.com/a/chromium.org/chromedriver/downloads

After downloading the file, we need to add its file path and location to our Python code.

The code below will open the browser and write "puan" to the YouTube live stream page every 5 minutes:


from selenium import webdriver
import time

# Start the WebDriver
browser = webdriver.Chrome('/path/to/chromedriver')

# Open the YouTube live stream page
browser.get('https://www.youtube.com/watch?v=VIDEO_ID')

while True:
    # Type "puan"
    chat_box = browser.find_element_by_xpath('//*[@id="chat-input"]')
    chat_box.send_keys('puan')
    chat_box.submit()
    
    # Wait for 5 minutes
    time.sleep(300)


You can try this code with the URL of your own YouTube live stream. The video ID is the combination of letters and numbers at the end of the YouTube URL, such as https://www.youtube.com/watch?v=ABCDEFGH.

Also, you can make the browser go into full screen mode after opening it with the following code:




# Go into full screen mode
browser.maximize_window()
