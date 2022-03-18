from .ytsearch import YouTubeSearch


class TestSearch:

    def test_init_defaults(self):
        search = YouTubeSearch('test')
        assert search.max_results is None
        assert 1 <= len(search.videos)

    def test_init_max_results(self):
        search = YouTubeSearch('test', max_results=10)
        assert 10 == search.max_results
        assert 10 == len(search.videos)

    def test_dict(self):
        search = YouTubeSearch('test', max_results=10)
        assert isinstance(search.to_dict(), list)

    def test_json(self):
        search = YouTubeSearch('test', max_results=10)
        assert isinstance(search.to_json(), str)

    def test_clear_cache(self):
        search = YouTubeSearch('test', max_results=10)
        json_output = search.to_json(clear_cache=False)
        assert "" != search.videos

        dict_output = search.to_dict()
        assert "" == search.videos
