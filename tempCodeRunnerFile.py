
# driver.get("https://www.google.com/")
# # # assert "Python" in driver.title
# # elem = driver.find_element(By.NAME, "q")
# # elem.clear()
# # elem.send_keys("pycon")
# # elem.send_keys(Keys.RETURN)
# # assert "No results found." not in driver.page_source
# input = driver.find_element(By.NAME, 'q')
# input.send_keys('numpy')
# time.sleep(2)

# input.send_keys(Keys.ENTER)

# data = driver.find_element(By.CLASS_NAME, 'LC20lb MBeuO DKV0Md').click()