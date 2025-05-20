from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

def crawl_daum_reviews(movie_url, max_pages=10):
    driver = webdriver.Chrome()
    driver.get(movie_url)
    reviews = []

    for _ in range(max_pages):
        time.sleep(1.5)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        comment_tags = soup.select('.cmt_box .desc_txt')
        for tag in comment_tags:
            reviews.append(tag.text.strip())

        try:
            next_btn = driver.find_element(By.CLASS_NAME, "link_page.next")
            next_btn.click()
        except:
            break

    driver.quit()
    return pd.DataFrame(reviews, columns=["review"])
