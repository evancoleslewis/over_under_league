import requests
import config
import logging

logging.basicConfig(filemode='w', filename='log/extract.log', level=logging.INFO)

def get_standings_html():
    """
    Requests hmtl from standings_url. Returns html.
    """

    with requests.Session() as session:
        response = session.get(config.STANDINGS_URL)
        text = response.text
        code = response.status_code

    if code != 200:
        logging.ERROR(f"Response status code: {code}\nResponse text:\n{text}")
        exit()

    logging.info(f"Successful Response:\n\n{text}")

    return text