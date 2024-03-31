import asyncio
from nba import NBA
from nfl import NFL
from mlb import MLB
import sys

async def main():
    # check if sys argv1 exists and assign to date else dat is null
    if len(sys.argv) > 1:
        date = sys.argv[1]
    else:
        date = None

    # Create an instance of the classes
    nba_instance = NBA()
    nfl_instance = NFL()
    mlb_instance = MLB()
    
    # Call the method on the instances
    await nba_instance.current_nba_matches("https://www.livescore.com/en/basketball/", date)
    # await mlb_instance.current_mlb_matches("https://evanalytics.com/mlb/odds", date)
    # await nfl_instance.current_nfl_matches("https://www.sofascore.com/american-football/", date)  
    

# Run the asyncio event loop
asyncio.run(main())
