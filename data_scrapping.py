import regex
import requests
import fitz
from bs4 import BeautifulSoup

def scrape_data_from_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all 'h2' tags (common for sub titles)
        all_titles = soup.find_all('h2')
        titles = []

        # Extract and print titles from 'h2' attributes
        for html_string1 in all_titles:
            html_string = str(html_string1)
            start_index = html_string.find('>')
            end_index = html_string.find('</h2>')
            if start_index != -1 and end_index != -1:
                title = html_string[start_index + 1: end_index]
                titles.append(title)
            else:
                print("No <h2> tag found or incorrect format")

        # Find all 'h3' tags (common for sub titles)
        all_sub_titles = soup.find_all('h3')
        sub_titles = []

        # Extract and print sub titles from 'h3' attributes
        for html_string1 in all_sub_titles:
            html_string = str(html_string1)
            start_index = html_string.find('>')
            end_index = html_string.find('</h3>')
            if start_index != -1 and end_index != -1:
                sub_title = html_string[start_index + 1: end_index]
                sub_titles.append(sub_title)
            else:
                print("No <h3> tag found or incorrect format")

        urls = []

        # Find all 'a' (anchor) tags that contain 'href' attribute (common for URLs)
        anchor_tags = soup.find_all('a', href=True)

        # Extract and print URLs from 'href' attributes
        for anchor in anchor_tags:
            urls.append(str(anchor['href']))
                                   
        # Extracting only the links using regular expressions
        extracted_links = [regex.findall(r'https?://\S+', url)[0] for url in urls if regex.findall(r'https?://\S+', url)]

        content = {
            "titles": titles,
            "subtitles": sub_titles,
            "links": extracted_links
        }
        return content
    else:
        return None  # Handle error cases accordingly
