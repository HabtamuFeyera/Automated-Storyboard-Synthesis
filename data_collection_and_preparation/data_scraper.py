import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape advertisement data from a website
def scrape_advertisements(url):
    # Send a GET request to the URL
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract advertisement descriptions and image URLs
        advertisements = []
        for ad in soup.find_all('div', class_='advertisement'):
            description = ad.find('p', class_='description').text
            image_url = ad.find('img')['src']
            advertisements.append({'description': description, 'image_url': image_url})
        return advertisements
    else:
        print("Failed to fetch data from the URL:", url)
        return []

# Function to save scraped data to a CSV file
def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['description', 'image_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    # Example usage
    url = 'https://example.com/advertisements'
    advertisements = scrape_advertisements(url)
    save_to_csv(advertisements, 'scraped_data.csv')
