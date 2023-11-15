import requests
import config
import logging

def get_standings_html(url):
    """
    Requests hmtl from url. Returns html.
    """

    with requests.Session() as session:
        response = session.get(url)
        text = response.text
        code = response.status_code

    if code != 200:
        logging.ERROR(f"Response status code: {code}\nResponse text:\n{text}")
        exit()

    logging.info(f"Successful HTML Extraction")

    return text