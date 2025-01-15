import time
import csv
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from urllib.robotparser import RobotFileParser

# Initialize logging for transparency
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Function to check robots.txt compliance
def check_robots_txt(base_url, user_agent):
    robots_url = f"{base_url}/robots.txt"
    logging.info(f"Checking robots.txt at {robots_url}...")
    
    rp = RobotFileParser()
    rp.set_url(robots_url)
    rp.read()
    return rp.can_fetch(user_agent, base_url)

# Base URL and User-Agent
base_url = "https://esla.wi.gov"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# Check robots.txt
if not check_robots_txt(base_url, user_agent):
    logging.error("Scraping is not allowed by the robots.txt file. Exiting...")
    exit(1)

# Add User-Agent to mimic a browser
chrome_options = Options()
chrome_options.add_argument("headless") # Run in headless mode (optional)
chrome_options.add_argument(f"user-agent={user_agent}")

# Initialize WebDriver
logging.info("Initializing WebDriver...")
driver = webdriver.Chrome(options=chrome_options)

# Target URL
url = "https://esla.wi.gov/inspectorlookup"

# Disclaimer for legal compliance
logging.info("Ensuring compliance with website terms of service and legal regulations.")
logging.info(
    "IMPORTANT: This script should only be used if scraping this website is allowed according to its terms of service."
)

# Open the page
logging.info("Opening the target URL...")
driver.get(url)
time.sleep(2)

# Select the Program Area dropdown
logging.info("Selecting 'Boiler and Unfired Pressure Vessels' from the dropdown...")
program_dropdown = Select(driver.find_element(By.ID, "j_id0:j_id70:programArea"))
program_dropdown.select_by_visible_text("Boiler and Unfired Pressure Vessels")
time.sleep(1)

# Click Search
logging.info("Clicking the 'Search' button...")
driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.searchButton").click()
time.sleep(3)

# Prepare CSV file
output_file = "inspectors_expanded.csv"
logging.info(f"Saving scraped data to {output_file}...")
with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Inspector Name", "Program Area", "Email", "Phone Number", "County"])

    # Scrape the table
    rows = driver.find_elements(By.CSS_SELECTOR, ".table.table-striped.no-footer.dataTable tbody tr")
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        inspector_name = cols[0].text
        program_area = cols[1].text

        # Extract Contact Information (both spans)
        contact_spans = cols[2].find_elements(By.TAG_NAME, "span")
        email = contact_spans[0].text if len(contact_spans) > 0 else ""
        phone = contact_spans[1].text if len(contact_spans) > 1 else ""

        # Split the County column into individual counties
        counties = cols[3].text.split(", ")

        # Create a row for each county
        for county in counties:
            writer.writerow([inspector_name, program_area, email, phone, county])
            logging.info(f"Added record for {inspector_name} in {county}.")

# Close WebDriver
driver.quit()
logging.info("Web scraping completed successfully.")

print(f"Data saved to {output_file}")
