# TrustATrader Web Scraping

This project performs web scraping on the TrustATrader website (https://www.trustatrader.com) to collect information about roofing and roofers companies in London.

## Requirements

- Python 3.x
- Beautiful Soup 4 library
- Requests library

You can install the required libraries with the following command:

```
pip install beautifulsoup4 requests
```

## Usage

Run the `trustatrader_scraper.py` file to start collecting information about roofing and roofers companies in London.

The script will go through 39 pages of results, collecting the following information for each company:

- Company name
- Address
- Phone number
- Website link (if available)

The collected information will be displayed in the standard output (console).

## Code

The main source code is in the `trustatrader_scraper.py` file. It uses the Requests library to make HTTP requests and the Beautiful Soup 4 library to parse and extract information from the HTML.

The script goes through 39 pages of results, making a request for each page and parsing the HTML to find the desired information.

## Limitations and improvements

- Currently, the script only collects information about roofing and roofers companies in London. You can modify the base URL to collect information from other locations or categories of companies.
- The script does not save the results to a file or database. You can add this functionality if desired.
- To avoid issues with the website, you can add a delay (using the `time.sleep()` function) between requests. This can help prevent your IP from being blocked by the site.

## License

This project is open source and is available under the MIT license. See the `LICENSE` file for more details.
