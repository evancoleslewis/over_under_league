import etl.extract as extract
import etl.transform as transform


def main():
    """
    Extracts html and parses for standings.
    """

    html = extract.get_standings_html()
    current_standings_df = transform.get_standings(html)
    print(current_standings_df)

    return

if __name__ == '__main__':
    main()

