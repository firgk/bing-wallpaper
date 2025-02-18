
import requests
import re

# Path to the README file
readme_file_path = 'README2.md'

# Function to download images
def download_image(i, url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"✅ [{i + 1}]: {file_name}")
    else:
        print(f"🥺 [{i + 1}]: Failed to download {url}")
# Function to scrape image URLs from README file
def scrape_image_urls(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regular expression to find all URLs that end with image file extensions
    image_urls = re.findall(r'(\d{4}-\d{2}-\d{2}) \[download 4k\]\((https?://[^\s]+\.jpg|png|jpeg|gif)', content)
    return image_urls

# Scrape image URLs from the README file
image_urls = list(scrape_image_urls(readme_file_path))

# Download each image
for i, url in enumerate(image_urls):
    print(url)
    file_name = url[0]+'--'+url[1].split('OHR.')[1]
    print(file_name)
    download_image(i, url[1], file_name)
