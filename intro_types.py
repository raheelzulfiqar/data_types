"""
Let's learn about Python types!
"""

import json

with open("raw_data/data.json", "r") as json_file:
    text = json_file.read()
    data = json.loads(text)
main_keys = data.keys()
print(f"the main keys are:{main_keys}")

language_code = data["LanguageCode"]
print(language_code)

search_parameters = data["SearchParameters"]
print('SearchParameters')

search_results = data["SearchResult"]
print('search_results')

search_results_keys = search_results.keys()
print(f"search result keys:{search_results_keys}")

search_results_count = search_results["SearchResultCount"]
print(search_results_count)

search_results_count_all = search_results["SearchResultCountAll"]
print(search_results_count_all)

search_results_items = search_results["SearchResultItems"]
print(search_results_items)







list_of_types = [type(item) for item in search_results_items]
print(list_of_types)

unique_types = set(list_of_types)
print(f"the unique types in list_of_types is:{unique_types}")

