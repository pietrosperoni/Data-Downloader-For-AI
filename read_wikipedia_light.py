import os
import requests
import argparse
from ai_summarizer import summarize_text

def fetch_wikipedia_page(title):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "page": title,
        "format": "json",
        "prop": "text",
        "utf8": 1,
        "formatversion": 2,
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["parse"]["text"]

def save_to_markdown(title, text):
    filename = f"{title}.md"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    print(f"File saved as: {filename}")

def save_to_file(title, text, file_extension="md"):
    filename = f"{title}.{file_extension}"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    print(f"File saved as: {filename}")

def save_to_file(title, text, folder_path, file_extension="md"):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    filename = os.path.join(folder_path, f"{title}.{file_extension}")
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    print(f"File saved as: {filename}")


def main():
    parser = argparse.ArgumentParser(description="Summarize a Wikipedia page with a given context")
    parser.add_argument("title", nargs="?", help="The title of the Wikipedia page")
    parser.add_argument("context", nargs="?", help="The context of interest for summarization")
    args = parser.parse_args()

    if args.title and args.context:
        wikipedia_title = args.title
        context = args.context
    else:
        wikipedia_title = input("Enter the title of the Wikipedia page: ")
        context = input("Enter the context of interest (leave empty for no context filtering): ")

    html_content = fetch_wikipedia_page(wikipedia_title)
    summary=summarize_text(html_content, context,500)

    print(summary)

    save_to_file(f"{wikipedia_title}_summary", summary, "outputs", "txt")
    quit()

if __name__ == "__main__":
    main()

