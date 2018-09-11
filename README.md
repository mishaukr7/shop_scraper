# shop_scraper
This is a Scrapy project to scrape information about suzy shier at  https://suzyshier.com/.

<h2>Extracted data</h2>
This project extracts all data including title, price, color etc..

<br>A sample item:
<pre><code>
{
"title": "Suzy Shier Fleece Lined Jogger Leggings", 
"price": "$24.00", 
"color": "Black",
"sizes": "S/M", 
"specs": "Model's Size: XSModel's Height: 5'10\"92% polyester, 8% spandex Machine wash in cold water, hang to dryDo not bleach",
"description": "The cool look of joggers mixes with the sleek fit of leggings in this comfy, fleece lined design."
}
</code></pre>

<h2>Spiders</h2>

This project contains two spiders: bottomscraper-css and exclusivescraper-css. 

<h2>Pipelines</h2>
This project contains two pipelines. 

<h2>Running the spiders</h2>
Data is stored in a file shop_data.json -  separately.

You can run a spider using the <i>scrapy crawl</i> command:

<pre><code>
$ scrapy crawl bottomscraper-css
$ scrapy crawl exclusivescraper-css
</code></pre>
