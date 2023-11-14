import config
import etl.extract as extract
import etl.transform as transform


def run():
    """
    Extracts html and parses for standings.
    """

    for run_type in config.RUN_TYPES:
        url = config.RUN_DICT[run_type]['url']
        html = extract.get_standings_html(url)
        standings_df = transform.get_standings(html, run_type)
        print(run_type, standings_df)

    return

if __name__ == '__main__':
    run()

