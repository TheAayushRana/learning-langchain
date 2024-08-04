from langchain_community.tools import TavilySearchResults

def get_profile_url_travily(name):
    search = TavilySearchResults();
    results = search.run(f"{name}")
    return results[0]['url']