from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from playsound import playsound

print("Launching code...")

options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome("chromedriver.exe", options=options)

print("Launching browser...")
time.sleep(0.5)
print("Getting all screenshots ready...")
time.sleep(0.5)
print("Approximate wait time 2 minutes 30 seconds")

"""Monito"""

# DEU to IND, 1000 EUR

driver.get("https://www.monito.com")

try:
    send_country_box_check = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.ID, "label-183"))
    )

    send_country_box = driver.find_element_by_id("label-183")
    send_country_box.click()
    send_country_box_search = driver.find_element_by_class_name("filter_1dXcM")
    send_country_box_search.clear()
    send_country_box_search.send_keys("Germany")
    send_country_box_search.send_keys(Keys.RETURN)

    receiver_country_box_check = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.ID, "label-186"))
    )

    receiver_country_box = driver.find_element_by_id("label-186")
    receiver_country_box.click()
    receiver_country_box_search = driver.find_element_by_class_name("filter_1dXcM")
    receiver_country_box_search.clear()
    receiver_country_box_search.send_keys("India")
    receiver_country_box_search.send_keys(Keys.RETURN)

    amount_box = driver.find_element_by_class_name("input_3IEKl")
    amount_box.clear()
    amount_box.send_keys("1000")
    amount_box.send_keys(Keys.RETURN)

    time.sleep(10)
    update_results_box = driver.find_element_by_xpath("//*[@id='__layout']/div/div/main/div/div[3]/div[2]/div[1]/div[2]/div/button")
    update_results_box.click()

    time.sleep(10)
except:
    driver.set_window_size(width=1877, height=1934)
    driver.get_screenshot_as_file('Monito_Deu_to_Ind_' + str(time.strftime("%Y%m%d_%H%M%S")) + '.png')

else:
    driver.set_window_size(width=1877, height=1934)
    driver.get_screenshot_as_file('Monito_Deu_to_Ind_' + str(time.strftime("%Y%m%d_%H%M%S")) + '.png')

# Return to the homepage

driver.back()

# AUS to IND, 1000 AUD

try:
    send_country_box_check = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.ID, "label-183"))
    )

    send_country_box = driver.find_element_by_id("label-183")
    send_country_box.click()
    send_country_box_search = driver.find_element_by_class_name("filter_1dXcM")
    send_country_box_search.clear()
    send_country_box_search.send_keys("Australia")
    send_country_box_search.send_keys(Keys.RETURN)

    receiver_country_box_check = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.ID, "label-186"))
    )

    receiver_country_box = driver.find_element_by_id("label-186")
    receiver_country_box.click()
    receiver_country_box_search = driver.find_element_by_class_name("filter_1dXcM")
    receiver_country_box_search.clear()
    receiver_country_box_search.send_keys("India")
    receiver_country_box_search.send_keys(Keys.RETURN)

    amount_box = driver.find_element_by_class_name("input_3IEKl")
    amount_box.clear()
    amount_box.send_keys("1000")
    amount_box.send_keys(Keys.RETURN)

    time.sleep(10)



    update_results_box = driver.find_element_by_xpath("//*[@id='__layout']/div/div/main/div/div[3]/div[2]/div[1]/div[2]/div/button")
    update_results_box.click()

    time.sleep(10)
except:
    driver.get_screenshot_as_file('Monito_Aus_to_Ind_' + str(time.strftime("%Y%m%d_%H%M%S")) + '.png')

else:
    driver.get_screenshot_as_file('Monito_Aus_to_Ind_' + str(time.strftime("%Y%m%d_%H%M%S")) + '.png')

# Return to the homepage

driver.back()

# GBR to IND, 1000 GBP

try:
    send_country_box_check = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.ID, "label-183"))
    )

    send_country_box = driver.find_element_by_id("label-183")
    send_country_box.click()
    send_country_box_search = driver.find_element_by_class_name("filter_1dXcM")
    send_country_box_search.clear()
    send_country_box_search.send_keys("United Kingdom")
    send_country_box_search.send_keys(Keys.RETURN)

    receiver_country_box_check = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.ID, "label-186"))
    )

    receiver_country_box = driver.find_element_by_id("label-186")
    receiver_country_box.click()
    receiver_country_box_search = driver.find_element_by_class_name("filter_1dXcM")
    receiver_country_box_search.clear()
    receiver_country_box_search.send_keys("India")
    receiver_country_box_search.send_keys(Keys.RETURN)

    amount_box = driver.find_element_by_class_name("input_3IEKl")
    amount_box.clear()
    amount_box.send_keys("1000")
    amount_box.send_keys(Keys.RETURN)

    time.sleep(10)



    update_results_box = driver.find_element_by_xpath("//*[@id='__layout']/div/div/main/div/div[3]/div[2]/div[1]/div[2]/div/button")
    update_results_box.click()

    time.sleep(10)
except:
    driver.get_screenshot_as_file('Monito_Gbr_to_Ind_' + str(time.strftime("%Y%m%d_%H%M%S")) + '.png')

else:
    driver.get_screenshot_as_file('Monito_Gbr_to_Ind_' + str(time.strftime("%Y%m%d_%H%M%S")) + '.png')

# Return to the homepage

driver.back()

# USA to IND, 1000 USD

try:
    send_country_box_check = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.ID, "label-183"))
    )

    send_country_box = driver.find_element_by_id("label-183")
    send_country_box.click()
    send_country_box_search = driver.find_element_by_class_name("filter_1dXcM")
    send_country_box_search.clear()
    send_country_box_search.send_keys("United States")
    send_country_box_search.send_keys(Keys.RETURN)

    receiver_country_box_check = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.ID, "label-186"))
    )

    receiver_country_box = driver.find_element_by_id("label-186")
    receiver_country_box.click()
    receiver_country_box_search = driver.find_element_by_class_name("filter_1dXcM")
    receiver_country_box_search.clear()
    receiver_country_box_search.send_keys("India")
    receiver_country_box_search.send_keys(Keys.RETURN)

    amount_box = driver.find_element_by_class_name("input_3IEKl")
    amount_box.clear()
    amount_box.send_keys("1000")
    amount_box.send_keys(Keys.RETURN)

    time.sleep(10)



    update_results_box = driver.find_element_by_xpath("//*[@id='__layout']/div/div/main/div/div[3]/div[2]/div[1]/div[2]/div/button")
    update_results_box.click()

    time.sleep(10)
except:
    driver.get_screenshot_as_file('Monito_Usa_to_Ind_' + str(time.strftime("%Y%m%d_%H%M%S")) + '.png')

else:
    driver.get_screenshot_as_file('Monito_Usa_to_Ind_' + str(time.strftime("%Y%m%d_%H%M%S")) + '.png')

# Return to the homepage

driver.back()

# ZAF to IND, 10,000 ZAR

try:
    send_country_box_check = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.ID, "label-183"))
    )

    send_country_box = driver.find_element_by_id("label-183")
    send_country_box.click()
    send_country_box_search = driver.find_element_by_class_name("filter_1dXcM")
    send_country_box_search.clear()
    send_country_box_search.send_keys("South Africa")
    send_country_box_search.send_keys(Keys.RETURN)

    receiver_country_box_check = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.ID, "label-186"))
    )

    receiver_country_box = driver.find_element_by_id("label-186")
    receiver_country_box.click()
    receiver_country_box_search = driver.find_element_by_class_name("filter_1dXcM")
    receiver_country_box_search.clear()
    receiver_country_box_search.send_keys("India")
    receiver_country_box_search.send_keys(Keys.RETURN)

    amount_box = driver.find_element_by_class_name("input_3IEKl")
    amount_box.clear()
    amount_box.send_keys("10000")
    amount_box.send_keys(Keys.RETURN)

    time.sleep(10)



    update_results_box = driver.find_element_by_xpath("//*[@id='__layout']/div/div/main/div/div[3]/div[2]/div[1]/div[2]/div/button")
    update_results_box.click()

    time.sleep(10)
except:
    driver.get_screenshot_as_file('Monito_Zaf_to_Ind_' + str(time.strftime("%Y%m%d_%H%M%S")) + '.png')

else:
    driver.get_screenshot_as_file('Monito_Zaf_to_Ind_' + str(time.strftime("%Y%m%d_%H%M%S")) + '.png')

# Return to the homepage

driver.back()

# IRL to IND, 1000 USD

try:
    send_country_box_check = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.ID, "label-183"))
    )

    send_country_box = driver.find_element_by_id("label-183")
    send_country_box.click()
    send_country_box_search = driver.find_element_by_class_name("filter_1dXcM")
    send_country_box_search.clear()
    send_country_box_search.send_keys("Ireland")
    send_country_box_search.send_keys(Keys.RETURN)

    receiver_country_box_check = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.ID, "label-186"))
    )

    receiver_country_box = driver.find_element_by_id("label-186")
    receiver_country_box.click()
    receiver_country_box_search = driver.find_element_by_class_name("filter_1dXcM")
    receiver_country_box_search.clear()
    receiver_country_box_search.send_keys("India")
    receiver_country_box_search.send_keys(Keys.RETURN)

    amount_box = driver.find_element_by_class_name("input_3IEKl")
    amount_box.clear()
    amount_box.send_keys("1000")
    amount_box.send_keys(Keys.RETURN)

    time.sleep(10)



    update_results_box = driver.find_element_by_xpath("//*[@id='__layout']/div/div/main/div/div[3]/div[2]/div[1]/div[2]/div/button")
    update_results_box.click()

    time.sleep(10)
except:
    driver.get_screenshot_as_file('Monito_Irl_to_Ind_' + str(time.strftime("%Y%m%d_%H%M%S")) + '.png')

else:
    driver.get_screenshot_as_file('Monito_Irl_to_Ind_' + str(time.strftime("%Y%m%d_%H%M%S")) + '.png')

# Return to the homepage

driver.back()

# NOR to IND, 1000 USD

try:
    send_country_box_check = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.ID, "label-183"))
    )

    send_country_box = driver.find_element_by_id("label-183")
    send_country_box.click()
    send_country_box_search = driver.find_element_by_class_name("filter_1dXcM")
    send_country_box_search.clear()
    send_country_box_search.send_keys("Norway")
    send_country_box_search.send_keys(Keys.RETURN)

    receiver_country_box_check = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.ID, "label-186"))
    )

    receiver_country_box = driver.find_element_by_id("label-186")
    receiver_country_box.click()
    receiver_country_box_search = driver.find_element_by_class_name("filter_1dXcM")
    receiver_country_box_search.clear()
    receiver_country_box_search.send_keys("India")
    receiver_country_box_search.send_keys(Keys.RETURN)

    amount_box = driver.find_element_by_class_name("input_3IEKl")
    amount_box.clear()
    amount_box.send_keys("1000")
    amount_box.send_keys(Keys.RETURN)

    time.sleep(10)



    update_results_box = driver.find_element_by_xpath("//*[@id='__layout']/div/div/main/div/div[3]/div[2]/div[1]/div[2]/div/button")
    update_results_box.click()

    time.sleep(10)
except:
    driver.get_screenshot_as_file('Monito_Nor_to_Ind_' + str(time.strftime("%Y%m%d_%H%M%S")) + '.png')

else:
    driver.get_screenshot_as_file('Monito_Nor_to_Ind_' + str(time.strftime("%Y%m%d_%H%M%S")) + '.png')

# Return to the homepage

driver.back()

# GBR to POL, 1000 USD

try:
    send_country_box_check = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.ID, "label-183"))
    )

    send_country_box = driver.find_element_by_id("label-183")
    send_country_box.click()
    send_country_box_search = driver.find_element_by_class_name("filter_1dXcM")
    send_country_box_search.clear()
    send_country_box_search.send_keys("United Kingdom")
    send_country_box_search.send_keys(Keys.RETURN)

    receiver_country_box_check = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.ID, "label-186"))
    )

    receiver_country_box = driver.find_element_by_id("label-186")
    receiver_country_box.click()
    receiver_country_box_search = driver.find_element_by_class_name("filter_1dXcM")
    receiver_country_box_search.clear()
    receiver_country_box_search.send_keys("Poland")
    receiver_country_box_search.send_keys(Keys.RETURN)

    amount_box = driver.find_element_by_class_name("input_3IEKl")
    amount_box.clear()
    amount_box.send_keys("1000")
    amount_box.send_keys(Keys.RETURN)

    time.sleep(10)

    update_results_box = driver.find_element_by_xpath("//*[@id='__layout']/div/div/main/div/div[3]/div[2]/div[1]/div[2]/div/button")
    update_results_box.click()

    time.sleep(10)
except:
    driver.get_screenshot_as_file('Monito_Gbr_to_Pol_' + str(time.strftime("%Y%m%d_%H%M%S")) + '.png')

else:
    driver.get_screenshot_as_file('Monito_Gbr_to_Pol_' + str(time.strftime("%Y%m%d_%H%M%S")) + '.png')

# COMPAREREMIT

driver.get("https://www.compareremit.com/compare-money-transfer-services-from-usd-to-india/?amt=1000&sc=USD&rc=INR")

# USA to IND, 1000 USD

time.sleep(10)

try:
    filter_box = driver.find_element_by_id("sort-toggle")
    filter_box.click()
    filter_box_best_value = driver.find_element_by_link_text("Best Value")
    filter_box_best_value.click()

    time.sleep(5)

except:
    driver.get_screenshot_as_file('CompareRemit_Usa_to_Ind_' + str(time.strftime("%Y%m%d_%H%M%S")) + '.png')

else:
    driver.get_screenshot_as_file('CompareRemit_Usa_to_Ind_' + str(time.strftime("%Y%m%d_%H%M%S")) + '.png')

# helloPaisa

driver.get("https://hellopaisa.co.za/")

# ZAR to INR, 10,000 ZAR

time.sleep(10)

try:
    receiver_country_box = driver.find_element_by_id("targetCountryFlag")
    receiver_country_box.click()
    receiver_country_box_search = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/ul/li[13]/img")
    receiver_country_box_search.click()


    amount_box = driver.find_element_by_id("fromInputValue")
    amount_box.clear()
    amount_box.send_keys("10000")
    amount_box.send_keys(Keys.RETURN)

    time.sleep(10)

except:
    driver.set_window_size(width=1000, height=1000)
    driver.execute_script("document.body.style.zoom='150%'")
    driver.get_screenshot_as_file('HelloPaisa_Zar_to_Inr_' + str(time.strftime("%Y%m%d_%H%M%S")) + '.png')

else:
    driver.set_window_size(width=1000, height=1000)
    driver.execute_script("document.body.style.zoom='150%'")
    driver.get_screenshot_as_file('HelloPaisa_Zar_to_Inr_' + str(time.strftime("%Y%m%d_%H%M%S")) + '.png')

# SBI

driver.get("https://za.statebank/home")

# ZAR to INR

time.sleep(5)

driver.set_window_size(width=450, height=800)
driver.get_screenshot_as_file('SBI_Zar_to_Inr_' + str(time.strftime("%Y%m%d_%H%M%S")) + '.png')

driver.quit()

print("Screenshots are ready")
playsound('Coin.mp3')

"""Zoom code: driver.execute_script("document.body.style.zoom='80%'")"""
"""Resolution code -  Large (default): driver.set_window_size(width=1877, height=1934)"""


