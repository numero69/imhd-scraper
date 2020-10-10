# imhd-scraper
Scrape news from iMHD.SK

:warning:**WARNING:** Using this project could lead to breaking [imhd TOS](https://imhd.sk/ba/doc/sk/10260/Podmienky-pou%C5%BE%C3%ADvania)

This python script can:
- Get the 20 latest news from **any** city supported by imhd.sk with info such as title, category and date posted
- Create an Microsoft Office Excel Sheet file with all the data scraped
- *soon*

**Changelog:**
- [x] Format the date to work with Excel and print at the same time
- [ ] Get the author of the doc
- [ ] Hyperlink to the doc


## What do you need for this to work:
1. BeatifulSoup4 - Get this by typing `pip install bf4` into your terminal
2. Python if using the source file

## How to use this scraper:
1. Run the file
2. Input the city code - [List of working city codes](CITIES.md)
3. Wait until the printing is finished
4. Your sheet is created in the same directory
