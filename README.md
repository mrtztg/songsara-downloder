[![GitHub release](https://img.shields.io/badge/release-v1.0-brightgreen?style=flat-square)](https://github.com/mrtztg/songsara-downloder/releases/tag/v1.0)
[![GitHub stars](https://img.shields.io/github/stars/mrtztg/songsara-downloder.svg?style=flat-square)](https://github.com/mrtztg/songsara-downloder/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/mrtztg/songsara-downloder.svg?style=flat-square)](https://github.com/mrtztg/songsara-downloder/network)
[![GitHub license](https://img.shields.io/github/license/mrtztg/songsara-downloder.svg?style=flat-square)](https://github.com/mrtztg/songsara-downloder/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/mrtztg/songsara-downloder.svg?style=flat-square)](https://github.com/mrtztg/songsara-downloder/udemy-dl/issues)

# SongSara Scraper & Downloader


#### Requirements


* Python >=3.4
* Python module `requests`
* Python module `BeautifulSoup`

#### How to use?


1. install required packages with `pip3 install -r requirements.txt` 
2. Copy pages' link to `input_url_list.txt`. One link per line.
3. Run script with: 
   ```ini
   python3 songsara.py
   ``` 
   
### What does script do?

* scrap and get links of songs in each page
* create a local folder for each page
* download each song to that if not exists