#Crawl PTT

import requests
from bs4 import BeautifulSoup

def crawl_article(url):
    r = requests.get(url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'html.parser') 
    metas = soup.select(".article-meta-value")
    main = soup.select("#main-content")

    data = {
        "日期": metas[3].text,
        "作者": metas[0].text,
        "標題": metas[2].text,
        "內文": main[0].text,
        "看板名稱": metas[1].text
    }

    #print(data)
    return data 

def crawler(name):
    base_url = "https://www.ptt.cc"
    start_url = "{}/bbs/{}/index.html".format(base_url, name)
    url = start_url
    
    while(1):
        print("page: {}".format(url))
        r = requests.get(url)
        html_doc = r.text
        
        soup = BeautifulSoup(html_doc, 'html.parser')
        #Get titles in the page
        a_titles = soup.select(".title a")
        for a in a_titles:
            #Get URL for the title
            article_url = "{}{}".format(base_url, a['href'])
            #Crawl data to get date,author,title,contents,groupname
            crawl_article(article_url)
        
        #Get button for prev/next page
        page_group = soup.select(".btn-group-paging .wide")
            
        try:
            #previous page
            next_url = page_group[1]['href']
        except:
            #until no previous page
            break  

        url = "{}{}".format(base_url, next_url)

def main(name):
    crawler(name)

if __name__ == "__main__":
    name = "Tech_Job"
    main(name)
