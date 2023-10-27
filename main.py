import requests
from bs4 import BeautifulSoup
import csv

# Replace the URL with the Amazon product page URL
url = 'https://www.amazon.com/b/?_encoding=UTF8&node=16225009011&pd_rd_w=OQd6G&content-id=amzn1.sym.5232c45b-5929-4ff0-8eae-5f67afd5c3dc&pf_rd_p=5232c45b-5929-4ff0-8eae-5f67afd5c3dc&pf_rd_r=A7VRDNP88MGPTXTP76M4&pd_rd_wg=ojLOo&pd_rd_r=98b65441-326c-4546-8dea-7bb2e16a932a&ref_=pd_gw_unk'

# Send an HTTP GET request to the URL
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Modify the following code to extract the specific data you need
    data_to_scrape = []
    for item in soup.find_all('your_html_element'):
        data = item.text  # You can modify this to extract specific data
        data_to_scrape.append(data)

    # You can choose to print the data on the console
    for data in data_to_scrape:
        print(data)

    # Or store the data in a CSV file
    with open('scraped_data.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Header1', 'Header2'])  # Replace with your column headers
        for data in data_to_scrape:
            # Modify the following line to match your data structure
            csvwriter.writerow([data, data])

else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
