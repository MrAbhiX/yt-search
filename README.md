# yt-search


Python function for searching for youtube videos to avoid using their heavily rate-limited API

To avoid using the API, this uses the form on the youtube homepage and scrapes the resulting page.

## Example Usage

For a basic search (and all of the current functionality), you can use the search tool as follows:

```pip install ytsearch```

```python
from ytsearch import YouTubeSearch

results = YouTubeSearch('search terms', max_results=10).to_json()

print(results)

# returns a json string

########################################

results = YouTubeSearch('search terms', max_results=10).to_dict()

print(results)
# returns a dictionary
```
