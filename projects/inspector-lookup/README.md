# Inspector Lookup Scraper

## Overview
This project scrapes the **Inspector Lookup** page of a given website.

## Features
1. Extracts Inspector Details (Name, Email, Phone Number, and County)
What It Does:
The script navigates to the Inspector Lookup page, selects the "Boiler and Unfired Pressure Vessels" program from a dropdown menu, and retrieves inspector details displayed in a dynamically generated HTML table.

## How It Works:

1. Browser Automation
The script uses Selenium WebDriver to automate interactions with the webpage, mimicking human actions such as:

Clicking buttons.
Selecting options from dropdown menus.

2. Dynamic Table Scraping
Selenium locates the table rows (<tr> elements) within the HTML structure and extracts data from the table cells (<td> elements). The extracted data includes:

* Inspector Name.
* Program Area.
* Email and Phone Number:

These are retrieved from <span> elements nested inside a cell.
* Counties:

A single cell containing a comma-separated list of counties is split into individual entries to create one row per county.

3. Saves the Data into a Structured CSV File
What It Does:
The extracted details are saved into a CSV file named inspectors_expanded.csv. The file includes the following columns:

Inspector Name
Program Area
Email
Phone Number
County

Outcome:
The resulting CSV file is clean and structured, with one row per inspector-county pair. This ensures compatibility with data analysis tools like Excel, Pandas, or BI platforms such as Tableau.

## Usage
Run the scraper:
```bash
git clone https://github.com/esamuel01/web-scraping-projects.git
cd web-scraping-projects/projects/inspector-lookup
python scraper.py
