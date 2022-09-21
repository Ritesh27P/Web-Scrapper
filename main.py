from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from flask import Flask, render_template, request, url_for
import time


driver_path = "D:\SetupFile\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(driver_path)
driver.get('https://news.google.com/')

news = []

data = driver.find_element(By.CLASS_NAME, 'DY5T1d').text
news.append(data)
print(data)

driver.get('https://news.google.com/')
input_search = driver.find_element(By.XPATH, "/html/body/div[4]/header/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]")
input_search.click();
input_search.send_keys('HDFC bank')
input_search.send_keys(Keys.ENTER);

content = driver.find_element(By.CLASS_NAME, 'xrnccd').text
print(content)
news.append(content)

input_search = driver.find_element(By.XPATH, '/html/body/div[4]/header/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]');
input_search.clear()
input_search.send_keys('WIPRO')
input_search.send_keys(Keys.ENTER)

content1 = driver.find_element(By.CLASS_NAME, 'ipQwMb ekueJc RD0gLb').text
news.append(content1)

print(news)
time.sleep(5);
driver.quit()

app = Flask(__name__)


@app.route('/')
def home():
    global news
    return render_template('index.html', data=news)


if __name__ == '__main__':
    app.run(debug=True)
