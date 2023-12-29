# -*- coding: utf-8 -*-
"""api_requests.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TVVis_0EAypNvc_hn5qVEXbi_S9j08W6
"""

import requests

def fetch_data_from_api(api_url):

    url = api_url
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        reponse_in_text_format =  response.text  # Assuming the API returns text data
    content = {
    "response_code": response.status_code,
    "response": reponse_in_text_format
    }
    return content