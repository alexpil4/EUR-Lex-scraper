import scrapy
from datetime import datetime

class EurlexSpider(scrapy.Spider):
    name = "eurlex"
    today = datetime.today().strftime("%d%m%Y")
    
    # Official Journal (OJ) page
    start_urls = [
        f"https://eur-lex.europa.eu/oj/daily-view/C-series/default.html?ojDate={today}&locale=en#"
    ]

    def parse(self, response):
        # Find the links to the Recruitment Notice notices and visit them one by one
        for link in response.css("a"):
            text = link.css("::text").get()
            href = link.css("::attr(href)").get()

            # Check it is a link to a Recruitment Notice (case-insensitive)
            if text and "recruitment notice" in text.lower() and href:
                if "?uri=OJ:C_" in href:
                    id_part = href.split("?uri=OJ:")[-1].strip()
                    html_doc_url = f'https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:{id_part}'

                    # Parse data via Scrapy parse_document
                    yield response.follow(html_doc_url, self.parse_document)

    def parse_document(self, response):
        # Get data from Recruitment Notice page
        title = response.xpath("//div[@id='tit_1']//p/text()").getall()

        # Looking for the doc publication date
        publication_date = response.css("p.oj-hd-date::text").get(default="No date").strip()

        # Looking for the doc main content
        content = " ".join(response.css("div p::text, div div p::text").getall()).strip()

        # Get expiration date of doc
        deadline = response.xpath("//p[contains(text(), 'deadline')]/following-sibling::p//span/text()").get()
        if deadline:
            deadline = deadline.strip()
        else:
            deadline = "Not specified"

        yield {
            "url": response.url,
            "title": title,
            "publication_date": publication_date,
            #The content here is limited to 2000 characters
            "content": content[:2000],
            "deadline": deadline
        }
