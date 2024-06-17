import requests
import json
import os

from langchain_core.tools import tool
from langchain_community.document_loaders import WebBaseLoader


class SearchTools:

    @tool('search internet')
    def search_internet(query: str) -> str:
        """
        Use this tool to search the internet for information.
        This tool return 5 results from Google search engine.
        """
        return SearchTools.search(query)

    @tool('search zhihu')
    def search_zhihu(query: str) -> str:
        """
        Use this tool to search the 知乎 platform for information.
        This tool return 5 results from 知乎 search engine.
        """
        return SearchTools.search(f"site:zhihu.com {query}")

    @tool('open page')
    def open_page(url: str) -> str:
        """
        Use this tool to open a webpage.
        This tool return the webpage content.
        """
        loader = WebBaseLoader(url)
        return loader.load()

    def search(query, limit=5):
        url = "https://google.serper.dev/search"
        payload = json.dumps({
            "q": query,
            "num": limit,
            "gl": "cn"
        })
        headers = {
            'X-API-KEY': os.getenv("SERPER_API_KEY"),
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        results = response.json()['organic']

        string = []
        for result in results:
            string.append(f"{result['title']}\n{result['snippet']}\n{result['link']}\n\n")

        return f"Search results for {query}:\n\n" + "\n".join(string)


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    #print(SearchTools.search_internet("如何挣一百万"))
    #print(SearchTools.search_zhihu("如何挣一百万"))
    print(SearchTools.open_page("https://www.python.org"))
