# scrapy learning project for MyMedic

https://github.com/LinkedInLearning/web-scraping-with-python-2848331


theory : 
#any span tag that has the class title 
#//span[@class="title"]/@id attribute id 
#text -> selector 

for css: 
/html/body/div/h1 -> have top follow hierarchy or 
//h1 for entire page 

in xpath : to get text, use text()
to get value of attribute use @attribute_name


commands :

#start project 
scrapy startproject basic_scrapper

#navigate to spiders 

#create spider
scrapy genspider ietf pythonscraping.com
- modify start_urls

#run spider 
scrapy runspider ietf.py

scrapy genspider wikipedia en.wikipedia.org

