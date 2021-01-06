#SongSara Scraper & Downloader


####Requirements
---
* Python >=3.4
* Python module `requests`
* Python module `BeautifulSoup`

####How to use?
___
1. install required packages with `pip3 install -r requirements.txt` 
2. Copy pages' link to `input_url_list.txt`. One link per line.
3. Run script with: 
   ```ini
   python3 songsara.py
   ``` 
   
###What does script do?
* scrap and get links of songs in each page
* create a local folder for each page
* download each song to that if not exists