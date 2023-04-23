from bs4 import BeautifulSoup
import time
import requests
import pandas as pd
import numpy as np

total_pages = range(1, 40)
for page in total_pages:
    url = f"https://www.trustatrader.com/search?trade_name=Roofers+&+Roofing=&search_trade_id=5b4cbdcc8811d346b846dac8&location_str=London&page={page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    li_tags = soup.find_all("li", class_='profile-card profile-card--guarantee')    
    for li_tag in li_tags:
        name = li_tag.find("h3", class_="profile-card__heading").text.strip()
        website_tags = li_tag.find("a", class_="profile-card__heading-link")
        websitehref = website_tags['href']
        website_response = requests.get("https://www.trustatrader.com" + websitehref)
        website_soup = BeautifulSoup(website_response.text, "html.parser")       
        #adress
        locality_tag = website_soup.find('span', itemprop="addressLocality")
        region_tag = website_soup.find('span', itemprop="addressRegion")
        postal_code_tag = website_soup.find('b', itemprop="postalCode")
        address_parts = []        
        if locality_tag:
            address_locality = locality_tag.text.strip()
            address_parts.append(address_locality)       
        if region_tag:
            address_region = region_tag.text.strip()
            address_parts.append(address_region)
        if postal_code_tag:
            postal_code = postal_code_tag.text.strip()
            address_parts.append(postal_code)        
        address = ', '.join(address_parts) if address_parts else "Address not found"      
        #Phone
        phone_tag = website_soup.find('span', itemprop="telephone")
        if phone_tag is not None:
            phone = phone_tag.text.strip()
        else:
            phone = "Phone not found"      
        #Link Site
        business_url = website_soup.find(class_="profile-opening__cta-link profile-opening__cta-link--website")
        if business_url is not None:
            rec = business_url.get('href')
        else:
            rec = "Website not found"
        #Business Infos
        print('Name:', name)
        print('Address:', address)
        print('Phone:', phone)
        print('link:', rec)
        print('-' * 80)