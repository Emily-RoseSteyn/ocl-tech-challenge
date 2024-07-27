from valuations.services.scraper import FullTitleScraper, SectionalTitleScraper


def main() -> None:
    FullTitleScraper().scrape()
    SectionalTitleScraper().scrape()


if __name__ == "__main__":
    main()
