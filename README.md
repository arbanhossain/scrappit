# Scrappit

Scrappit is a web-scraper for reddit with a command line interface.

### Usage
- Clone or download the repo
- Run ```python scrappit.py```. This should show you the arguments needed for the tool

##### Arguments
- ```subreddit```: This is the only required argument for the tool. Enter the name of the subreddit you wish to scrape. You can use it followingly:
  ```bash
  python scrappit.py writing
  ```
- ```-f```: If you wish to only see posts with a specific flair, use this option followed by the desired flair name. Such as:
  ```bash
  python scrappit.py writing -f Advice
  ```
- ```-k```: If you wish to only see posts related to something or having a specific word in it, use this this option followed by the keywords. Like:
  ```bash
  python scrappit.py writing -f Advice -k new character future books
  ```
