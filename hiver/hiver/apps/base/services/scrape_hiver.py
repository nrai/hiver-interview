"""
Extracting after scrapping the web page
"""
import operator
from urllib.request import urlopen
from lxml.html.clean import Cleaner
from bs4 import BeautifulSoup


def find_commonly_used_words():
    # Extract HTML content from website
    html_content = scrape_website('https://hiverhq.com')
    # Cleaning Javascript and Style
    cleaner_content = remove_script_and_style(html_content)
    # Getting Content between tags
    text_content = extract_text_content(cleaner_content)
    # Remove \n and \t from html
    text = remove_tabs_newline_whitespaces(text_content)
    # Find occurences of each character
    word_dictionary = each_word_occurrence(text)
    # Print Top 5 words with their number of occurrences
    sorted_words_dict = return_sorted_elements(word_dictionary, 5)
    print(sorted_words_dict)


def scrape_website(url):
    html = urlopen(url).read().decode('utf-8')
    return html


def remove_script_and_style(html_content):
    cleaner = Cleaner()
    cleaner.javascript = True
    cleaner.style = True
    cleaner.kill_tags = ['script']
    clean_html = cleaner.clean_html(html_content)
    return clean_html


def extract_text_content(cleaner_content):
    return BeautifulSoup(cleaner_content, 'lxml').text


def remove_tabs_newline_whitespaces(text_content):
    text_content = text_content.replace('\n', ' ')
    text_content = text_content.replace('\t', ' ')
    text_content = text_content.strip()
    return text_content


def each_word_occurrence(text):
    word_dictionary = dict()
    words = text.split()
    for word in words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    return word_dictionary


def return_sorted_elements(word_dictionary, count=0):
    sorted_words = sorted(word_dictionary.items(), key=operator.itemgetter(1))
    sorted_words.reverse()
    if count != 0:
        return sorted_words[:count]
    else:
        return sorted_words
