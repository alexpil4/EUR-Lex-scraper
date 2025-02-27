# Eurlex Scrapy Spider Documentation

## Overview
This repository contains a Scrapy spider to scrape **Recruitment Notice** pages from the Official Journal (OJ) of the European Union published on the Eur-Lex platform. The spider fetches detailed data about these notices, including title, publication date, content, and the application deadline.

## Project Structure
```
eurlex_scraper/
├── eurlex_spider.py         # Contains the EurlexSpider implementation
├── requirements.txt         # Python dependencies
├── LICENSE                  # License file (AGPL-3.0)
└── README.md                # Project documentation (this file)
```

## Prerequisites
- Python 3.6+ 
- Scrapy 2.0 or higher

You can install the required dependencies using:

```bash
pip install -r requirements.txt
```

## How to Use

### Step 1: Install Dependencies

```bash
pip install scrapy
```

### Step 2: Running the Spider

To run the spider, navigate to the project directory and use the following command:

```bash
scrapy crawl eurlex -o documents.json
```

### Step 3: Output

The spider will output scraped data, including:

```json
{
  "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:C_2022_0125_01",
  "title": ["Recruitment Notice", "European Commission - Contract Agent vacancies"],
  "publication_date": "01 January 2025",
  "content": "The European Commission is seeking applicants for contract agent positions...",
  "deadline": "15 February 2025"
}
```

## License

This project is licensed under the **GNU Affero General Public License (AGPL-3.0)**. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork and submit pull requests for improvements, bug fixes, or new features.

For any issues, open an issue in the repository.

