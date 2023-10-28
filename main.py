import etl.extract.extract as extract

def main():
    """
    Extracts html and parses for standings.
    """

    html = extract.get_standings_html()

    return

if __name__ == '__main__':
    main()

