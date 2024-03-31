from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import asyncio
import time

class NBA:
    def __init__(self):
        pass

    async def current_nba_matches(self, url, date):
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
                status_elements = soup.find_all('div', class_='Hp')


                # Check if any elements were found
                if status_elements:
                    print("Below are all the NBA GAMES scraped:")
                    print(f"Total games Found: {len(status_elements)}")
                    for status_element in status_elements:
                        up = status_element.find('div', class_='up')
                        home_team_odds = status_element.find('div', class_='Bp')
                        away_team_odds = status_element.find('div', class_='Cp')
                        up = status_element.find('div', class_='up')
                        home_team = up.find('div', class_='wp')
                        home_team_logo = status_element.find('img')
                        vp = status_element.find('div', class_='vp')
                        away_team = vp.find('div', class_='wp')
                        away_team_logo = vp.find('img')

                        team_data = {}
                        if home_team:
                            team_data['home_team'] = home_team.text
                        if away_team:
                            team_data['away_team'] = away_team.text
                        if home_team_odds:
                            team_data['home_team_odds'] = home_team_odds.text
                        if away_team_odds:
                            team_data['away_team_odds'] = away_team_odds.text
                        if home_team_logo:
                            team_data['home_team_logo'] = home_team_logo['src']
                        if away_team_logo:
                            team_data['away_team_logo'] = away_team_logo['src']

                        teams.append(team_data)

                    for team in teams:
                        print(f"Home Team: {team.get('home_team', 'N/A')}")
                        print(f"Away Team: {team.get('away_team', 'N/A')}")
                        print(f"Home Team Odds: {team.get('home_team_odds', 'N/A')}")
                        print(f"Away Team Odds: {team.get('away_team_odds', 'N/A')}")
                        print(f"Home Team Logo: {team.get('home_team_logo', 'N/A')}")
                        print(f"Away Team Logo: {team.get('away_team_logo', 'N/A')}")
                        print()
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


