from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import asyncio
import time

class MLB:
    def __init__(self):
        pass

    async def current_mlb_matches(self, url, date):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        teams = []  # Initialize the variable outside the loop

        while True:  # Keep trying until elements with class 'Hp' are found
            try:
                # Initialize the Chrome driver with the headless option
                driver = webdriver.Chrome(options=chrome_options)
                # Make a request to the webpage
                driver.get(f"{url}/{date}")
                # You might need to adjust the wait time based on the actual loading time of the element
                driver.implicitly_wait(10) # Wait up to 10 seconds

                # Parse the HTML content
                soup = BeautifulSoup(driver.page_source, "html.parser")

                # Find all elements with class 'Hp'
                status_elements = soup.find_all('table', class_='eva-odds-table')

 
                # Check if any elements were found
                if status_elements:
                    print("Below are all the MLB GAMES scraped:")
                    print(f"Total games Found: {len(status_elements)}")
                    
                    print('Teams Scraping Completed')
                    break  # Exit the loop if data is successfully scraped
                else:
                    print("No elements with class 'Hp' were found. Retrying...")
                    time.sleep(5)  # Wait for 5 seconds before retrying

            except Exception as e:
                print(f"An error occurred: {e}")
                print("Retrying...")
                time.sleep(5)  # Wait for 5 seconds before retrying

            finally:
                # Close the browser to avoid resource leaks
                if 'driver' in locals():
                    driver.quit()

        return teams  # Return the list of teams


