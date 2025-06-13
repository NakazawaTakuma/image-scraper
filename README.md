# Image Scraper

A Selenium-based Python script to automatically download images from Google Images based on a list of search terms.

## Features

- Reads search terms from a text file (`items_list.txt`).
- Creates a structured directory for each term or category.
- Searches Google Images (optionally with an extra keyword) in headless mode.
- Downloads a configurable number of images per term and converts them to JPEG.

## Prerequisites

- Python 3.8+
- Google Chrome browser installed

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/image-scraper.git
   cd image-scraper
   ```

````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Prepare your items list:
   Create `items_list.txt` in the project root, listing one search term per line. Use lines starting with `#` for comments and single letters to mark folder sections.

## Usage

```bash
python main.py --input items_list.txt --output images --max-images 30 --suffix "underwater"
```

- `--input`: Path to your items list text file.
- `--output`: Output directory for downloaded images.
- `--max-images`: (Optional) Maximum number of images per term (default: 30).
- `--suffix`: (Optional) Additional keyword to append to each search term (default: none).

## Project Structure

- `main.py`: Main scraping script.
- `requirements.txt`: Python dependencies.
- `.gitignore`: Git ignore rules.

## License

MIT License
````
