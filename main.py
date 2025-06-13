import os
import re
import argparse
import datetime
import urllib.request
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image


def parse_args():
    parser = argparse.ArgumentParser(description="Generic Image Scraper")
    parser.add_argument(
        '--input', '-i', type=str, default='items_list.txt',
        help='Path to the list of search terms.'
    )
    parser.add_argument(
        '--output', '-o', type=str, default='images',
        help='Directory to save downloaded images.'
    )
    parser.add_argument(
        '--max-images', '-m', type=int, default=30,
        help='Maximum images per search term.'
    )
    parser.add_argument(
        '--suffix', '-s', type=str, default='',
        help='Optional keyword to append to each search term.'
    )
    return parser.parse_args()


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


def sanitize_name(name):
    # Remove parenthesized text and trailing whitespace
    return re.sub(r"\(.+?\)", "", name).strip()


def download_images(driver, query, save_dir, max_images):
    driver.get('https://www.google.com/imghp?hl=en')
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys(query, Keys.ENTER)

    first_thumb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.rg_i.Q4LuWd'))
    )
    driver.execute_script("arguments[0].click();", first_thumb)

    count = 0
    while count < max_images:
        try:
            img = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'img.r48jcc.pT0Scc.iPVvYb'))
            )
            url = img.get_attribute('src')
            if not url or not url.startswith('http'):
                raise Exception('Invalid URL')

            filename = f"{count+1}_{query.replace(' ', '_')}.jpg"
            filepath = os.path.join(save_dir, filename)
            urllib.request.urlretrieve(url, filepath)

            try:
                im = Image.open(filepath)
                im.convert('RGB').save(filepath, 'JPEG')
            except:
                pass

            count += 1
            print(f"Downloaded {count}/{max_images}: {filename}")

            next_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[aria-label="Next"]'))
            )
            next_btn.click()
            sleep(1)
        except Exception as e:
            print(f"Error on image {count+1}: {e}")
            break


def main():
    args = parse_args()
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))

    os.makedirs(args.output, exist_ok=True)

    with open(args.input, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    driver = setup_driver()
    current_folder = None

    for line in lines:
        if not line.strip() or line.startswith('#'):
            continue
        if len(line.strip()) == 1:
            # Section folder
            current_folder = os.path.join(args.output, line.strip())
            os.makedirs(current_folder, exist_ok=True)
        else:
            term = sanitize_name(line)
            query = f"{term} {args.suffix}".strip()
            subfolder = term.replace(' ', '_')
            save_dir = os.path.join(current_folder or args.output, subfolder)
            os.makedirs(save_dir, exist_ok=True)
            download_images(driver, query, save_dir, args.max_images)

    driver.quit()

if __name__ == '__main__':
    main()