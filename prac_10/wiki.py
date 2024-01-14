import wikipedia

def main():
    while True:
        search_input = input("Enter a page title or search phrase (blank to exit): ").strip()
        if not search_input:
            break
        get_wikipedia_page(search_input)
def get_wikipedia_page(title):
    try:
        page = wikipedia.page(title, autosuggest=False)
        print("Title:", page.title)
        print("Summary:", page.summary)
        print("URL:", page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Disambiguation: {e.options}")


if __name__ == "__main__":
    main()
