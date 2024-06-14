import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Replace 'path/to/chromedriver' with the path to your downloaded driver executable
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.medica-tradefair.com/vis/v1/en/search?ticket=g_u_e_s_t&_query=&f_type=profile')

# Function to continuously scroll down the page until all content is loaded
def scroll_down():
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Adjust the sleep time as needed
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# Add a delay to allow the page to load
time.sleep(3)  # Adjust the sleep time as needed

# Scroll down to load all content
scroll_down()

# Find all company elements within the searchresult-item class
companies = driver.find_elements(By.CSS_SELECTOR, ".searchresult-item .media__body__head")
locations = driver.find_elements(By.CSS_SELECTOR, ".searchresult-item .media__body__head-sub")

# Print the text content of each company element
for company, location in zip(companies, locations):
    print(company.text)
    print(location.text)
    print('---')  # Add a separator between company names and locations

csv_file_path = 'company_info.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Company Name', 'Location'])  # Write the header row
    
    # Write each company name and location to the CSV file
    for company, location in zip(companies, locations):
        writer.writerow([company.text, location.text])    

# Close the WebDriver
driver.quit()
