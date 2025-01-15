# Inspector Lookup Scraper

## Overview
This project scrapes the **Inspector Lookup** page of a given website.

## Features
1. Extracts Inspector Details (Name, Email, Phone Number, and County)
What It Does:
The script navigates to the Inspector Lookup page, selects the "Boiler and Unfired Pressure Vessels" program from a dropdown menu, and retrieves inspector details displayed in a dynamically generated HTML table.

How It Works:

Browser Automation:
The script uses Selenium WebDriver to automate interactions with the webpage, mimicking human actions like clicking buttons and selecting dropdown options.

Dynamic Table Scraping:
Selenium locates the table rows (<tr> elements) within the HTML structure and extracts data from the cells (<td> elements) corresponding to:
Inspector Name
Program Area
Email and Phone Number (retrieved from <span> elements inside a cell)
Counties (split into individual entries from a comma-separated list)

2. Saves the Data into a Structured CSV File
What It Does:
The extracted details are saved into a CSV file (inspectors_expanded.csv) for easy analysis and future use.

Outcome:
The resulting CSV file is well-organized, with a row for every inspector-county pair. This ensures compatibility with data analysis tools like Excel, Pandas, or BI platforms.

## Usage
Run the scraper:
```bash
git clone https://github.com/esamuel01/web-scraping-projects.git
cd web-scraping-projects/projects/inspector-lookup
python scraper.py
