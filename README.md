# Scrapper

[Reference](https://realpython.com/beautiful-soup-web-scraper-python/)

## URL

- base URL
- the specific site location

## Query parameters

```txt
?q=software+developer&l=Australia
```

- start `?`
- information `key=value`
- separator `&`

## Exploring the URLs of a site

## Using Developer tools to explore the sites DOM.

## Installation of Python3

```sh
brew install python
python3 --version
python3

python3 -m pip // check pip
python3 -m pip install requests //install requests
```

## Handling authentication

to scrappe information behind the login

## Static website vs dynamic website

when you make HTTP request on dynamic website, the server will send you back some javascript code instead of HTML.

you need `requests-html` to render javascript.

Another tool for scraping dynamic content is selenium.

## Parse HTML Code with Beautiful Soup

Beautiful Soup is a python library for parsing structured data.

```sh
python3 -m pip install beautifulsoup4
```

## beautiful soup APIs

```py
element.get(ATTRIBUTE)
```
