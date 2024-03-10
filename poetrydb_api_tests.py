import unittest
import requests

class TestHTTP(unittest.TestCase):

    """
    response = TestHttp.get('/some_endpoint')
    puts response.body
    puts response.code  

    """

    # TEST HOMEPAGE
    def test_home_page(self):
        response = requests.get('/')
        self.assertIn('PoetryDB is the world\'s first API for next generation internet poets', response.text)
        self.assertEqual(response.status_code, 200)

    def test_author_search(self):
        response = requests.get('/author')
        self.assertIn('Ernest Dowson', response.text)
        self.assertIn('Emily Dickinson', response.text)
        self.assertEqual(response.status_code, 200)

        response = requests.get('/authors')
        self.assertIn('Ernest Dowson', response.text)
        self.assertIn('Emily Dickinson', response.text)
        self.assertEqual(response.status_code, 200)

        response = requests.get('/author/Dowson')
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_author_text_format(self):
        response = requests.get('/author/Dowson/title,lines,author.text')
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn("title\n", response.text)
        self.assertIn("author\n", response.text)
        self.assertIn("lines\n", response.text)
        self.assertNotIn("linecount\n", response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_author_json_format(self):
        response = requests.get('/author/Dowson/title,lines,author.json')
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertNotIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_author_all_fields(self):
        response = requests.get('/author/Dowson/all')
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_author_all_fields_text_format(self):
        response = requests.get('/author/Dowson/all.text')
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn("title\n", response.text)
        self.assertIn("author\n", response.text)
        self.assertIn("lines\n", response.text)
        self.assertIn("linecount\n", response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_author_all_fields_json_format(self):
        response = requests.get('/author/Dowson/all.json')
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    # TEST TITLES
    def test_list_all_titles_method_1(self):
        response = requests.get('/title')
        self.assertIn('Bereavement in their death to feel', response.text)
        self.assertIn('Said Death to Passion', response.text)
        self.assertIn('The Moon Maiden\'s Song', response.text)
        self.assertEqual(response.status_code, 200)

    def test_list_all_titles_method_2(self):
        response = requests.get('/titles')
        self.assertIn('Bereavement in their death to feel', response.text)
        self.assertIn('Said Death to Passion', response.text)
        self.assertIn('The Moon Maiden\'s Song', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_title(self):
        response = requests.get("/title/The%20Moon%20Maiden's%20Song")
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_title_return_some_output_fields_text_format(self):
        response = requests.get("/title/The%20Moon%20Maiden's%20Song/title,lines,author.text")
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn("title\n", response.text)
        self.assertIn("author\n", response.text)
        self.assertIn("lines\n", response.text)
        self.assertNotIn("linecount\n", response.text)
        self.assertEqual(response.status_code, 200)
    
    def test_search_by_title_return_some_output_fields_format_as_json(self):
        response = requests.get("/title/The%20Moon%20Maiden's%20Song/title,lines,author.json")
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertNotIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_title_return_all_output_fields(self):
        response = requests.get("/title/The%20Moon%20Maiden's%20Song/all")
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_title_return_all_output_fields_format_as_text(self):
        response = requests.get("/title/The%20Moon%20Maiden's%20Song/all.text")
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn("title\n", response.text)
        self.assertIn("author\n", response.text)
        self.assertIn("lines\n", response.text)
        self.assertIn("linecount\n", response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_title_return_all_output_fields_format_as_json(self):
        response = requests.get("/title/The%20Moon%20Maiden's%20Song/all.json")
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    # TEST LINES SEARCH
    def test_search_by_lines(self):
        response = requests.get('/lines/Love%20stays%20a%20summer%20night')
        self.assertIn("The Moon Maiden's Song", response.text)
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_lines_return_some_output_fields_format_as_text(self):
        response = requests.get('/lines/Love%20stays%20a%20summer%20night/title,lines,author.text')
        self.assertIn("The Moon Maiden's Song", response.text)
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn("title\n", response.text)
        self.assertIn("author\n", response.text)
        self.assertIn("lines\n", response.text)
        self.assertNotIn("linecount\n", response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_lines_return_some_output_fields_format_as_json(self):
        response = requests.get('/lines/Love%20stays%20a%20summer%20night/title,lines,author.json')
        self.assertIn("The Moon Maiden's Song", response.text)
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertNotIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_lines_return_all_output_fields(self):
        response = requests.get('/lines/Love%20stays%20a%20summer%20night/all')
        self.assertIn("The Moon Maiden's Song", response.text)
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_lines_return_all_output_fields_format_as_text(self):
        response = requests.get('/lines/Love%20stays%20a%20summer%20night/all.text')
        self.assertIn("The Moon Maiden's Song", response.text)
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn("title\n", response.text)
        self.assertIn("author\n", response.text)
        self.assertIn("lines\n", response.text)
        self.assertIn("linecount\n", response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_lines_return_all_output_fields_format_as_json(self):
        response = requests.get('/lines/Love%20stays%20a%20summer%20night/all.json')
        self.assertIn("The Moon Maiden's Song", response.text)
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    # TEST LINE COUNT SEARCH
    def test_search_by_linecount(self):
        response = requests.get('/linecount/16')
        self.assertIn("The Moon Maiden's Song", response.text)
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_linecount_return_some_output_fields_format_as_text(self):
        response = requests.get('/linecount/16/title,lines,author.text')
        self.assertIn("The Moon Maiden's Song", response.text)
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn("title\n", response.text)
        self.assertIn("author\n", response.text)
        self.assertIn("lines\n", response.text)
        self.assertNotIn("linecount\n", response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_linecount_return_some_output_fields_format_as_json(self):
        response = requests.get('/linecount/16/title,lines,author.json')
        self.assertIn("The Moon Maiden's Song", response.text)
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertNotIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_linecount_return_all_output_fields(self):
        response = requests.get('/linecount/16/all')
        self.assertIn("The Moon Maiden's Song", response.text)
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_linecount_return_all_output_fields_format_as_text(self):
        response = requests.get('/linecount/16/all.text')
        self.assertIn("The Moon Maiden's Song", response.text)
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn("title\n", response.text)
        self.assertIn("author\n", response.text)
        self.assertIn("lines\n", response.text)
        self.assertIn("linecount\n", response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_linecount_return_all_output_fields_format_as_json(self):
        response = requests.get('/linecount/16/all.json')
        self.assertIn("The Moon Maiden's Song", response.text)
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    # TEST POEM COUNT SEARCH
    def test_find_1_poem(self):
        response = requests.get('/poemcount/1')
        self.assertNotIn('},', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_find_1_poem_return_some_output_fields_format_as_text(self):
        response = requests.get('/poemcount/1/title,lines,author.text')
        self.assertNotIn('},', response.text)
        self.assertIn("title\n", response.text)
        self.assertIn("author\n", response.text)
        self.assertIn("lines\n", response.text)
        self.assertNotIn("linecount\n", response.text)
        self.assertEqual(response.status_code, 200)

    def test_find_1_poem_return_some_output_fields_format_as_json(self):
        response = requests.get('/poemcount/1/title,lines,author.json')
        self.assertNotIn('},', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertNotIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_find_1_poem_return_all_output_fields(self):
        response = requests.get('/poemcount/1/all')
        self.assertNotIn('},', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_find_1_poem_return_all_output_fields_format_as_text(self):
        response = requests.get('/poemcount/1/all.text')
        self.assertNotIn('},', response.text)
        self.assertIn("title\n", response.text)
        self.assertIn("author\n", response.text)
        self.assertIn("lines\n", response.text)
        self.assertIn("linecount\n", response.text)
        self.assertEqual(response.status_code, 200)

    def test_find_1_poem_return_all_output_fields_format_as_json(self):
        response = requests.get('/poemcount/1/all.json')
        self.assertNotIn('},', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_find_2_poems_return_all_output_fields_format_as_json(self):
        response = requests.get('/poemcount/2/all.json')
        self.assertIn('},', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    # TEST RANDOM SEARCH
    def test_find_1_random_poem(self):
        response = requests.get('/random/1')
        self.assertNotIn('},', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_find_1_random_poem_return_some_output_fields_format_as_text(self):
        response = requests.get('/random/1/title,lines,author.text')
        self.assertNotIn('},', response.text)
        self.assertIn("title\n", response.text)
        self.assertIn("author\n", response.text)
        self.assertIn("lines\n", response.text)
        self.assertNotIn("linecount\n", response.text)
        self.assertEqual(response.status_code, 200)

    def test_find_1_random_poem_return_some_output_fields_format_as_json(self):
        response = requests.get('/random/1/title,lines,author.json')
        self.assertNotIn('},', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertNotIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_find_1_random_poem_return_all_output_fields(self):
        response = requests.get('/random/1/all')
        self.assertNotIn('},', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_find_1_random_poem_return_all_output_fields_format_as_text(self):
        response = requests.get('/random/1/all.text')
        self.assertNotIn('},', response.text)
        self.assertIn("title\n", response.text)
        self.assertIn("author\n", response.text)
        self.assertIn("lines\n", response.text)
        self.assertIn("linecount\n", response.text)
        self.assertEqual(response.status_code, 200)

    def test_find_1_random_poem_return_all_output_fields_format_as_json(self):
        response = requests.get('/random/1/all.json')
        self.assertNotIn('},', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_find_2_random_poems_return_all_output_fields_format_as_json(self):
        response = requests.get('/random/2/all.json')
        self.assertIn('},', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    # TEST COMBINATION SEARCH
    def test_search_by_author_title_return_some_output_fields_format_as_json(self):
        response = requests.get('/author,title/Dowson;Moon/title,lines,linecount')
        self.assertIn('Love stays a summer night', response.text)
        self.assertIn('"title":', response.text)
        self.assertNotIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_author_linecount_exactly_return_some_output_fields(self):
        response = requests.get('/author,linecount/Dowson;16:abs/title,lines,linecount')
        self.assertIn('Love stays a summer night', response.text)
        self.assertIn('"title":', response.text)
        self.assertNotIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_author_title(self):
        response = requests.get('/author,title/Dickinson;Said%20Death%20to%20Passion')
        self.assertIn('And the Debate was done.', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    # TEST 404
    def test_search_by_author_linecount_when_no_linecount_matches(self):
        response = requests.get('/author,linecount/Dowson;6/title,lines,linecount')
        self.assertNotIn('Love stays a summer night', response.text)
        self.assertIn('404', response.text)
        self.assertIn('Not found', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_author_linecount_exactly_when_no_linecount_matches(self):
        response = requests.get('/author,linecount/Dowson;6:abs/title,lines,linecount')
        self.assertNotIn('Love stays a summer night', response.text)
        self.assertIn('404', response.text)
        self.assertIn('Not found', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_author_title_exactly_when_no_title_matches(self):
        response = requests.get('/author,title/Dickinson;Said:abs')
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertIn('404', response.text)
        self.assertIn('Not found', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_author_exactly_title_exactly_when_no_author_matches(self):
        response = requests.get('/author,title/Dickinson:abs;Said%20Death%20to%20Passion:abs')
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertIn('404', response.text)
        self.assertIn('Not found', response.text)
        self.assertEqual(response.status_code, 200)

    # TEST 405 INVALID INPUT
    def test_search_by_invalid_input_field(self):
        response = requests.get('/wrong')
        self.assertIn('405', response.text)
        self.assertIn('list not available. Only author and title allowed.', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_invalid_input_field_with_corresponding_search_field(self):
        response = requests.get('/wrong/Dowson')
        self.assertIn('405', response.text)
        self.assertIn('input field not available. Only author, title, lines, linecount, and poemcount or random allowed.', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_invalid_input_field_return_all_output_fields_format_text(self):
        response = requests.get('/wrong/Dowson/all.text')
        self.assertIn('405', response.text)
        self.assertIn('input field not available. Only author, title, lines, linecount, and poemcount or random allowed.', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_invalid_input_field_return_all_output_fields_format_json(self):
        response = requests.get('/wrong/Dowson/all.json')
        self.assertIn('405', response.text)
        self.assertIn('input field not available. Only author, title, lines, linecount, and poemcount or random allowed.', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_combination_of_invalid_and_valid_input_fields_exactly_return_some_output_fields(self):
        response = requests.get('/wrong,linecount/Dowson;16:abs/title,lines,linecount')
        self.assertNotIn('Love stays a summer night', response.text)
        self.assertIn('405', response.text)
        self.assertIn('input field not available. Only author, title, lines, linecount, and poemcount or random allowed.', response.text)
        self.assertEqual(response.status_code, 200)

     # TEST 405 INVALID OUTPUT FIELDS
    def test_search_by_author_return_some_output_fields_format_as_invalid_format(self):
        response = requests.get('/author/Dowson/title,lines,author.wrong')
        self.assertNotIn('Love stays a summer night', response.text)
        self.assertIn('405', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_author_return_all_output_fields_format_as_invalid_format(self):
        response = requests.get('/author/Dowson/all.wrong')
        self.assertNotIn('Love stays a summer night', response.text)
        self.assertIn('405', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_author_return_invalid_output_field(self):
        response = requests.get('/author/Dowson/titles')
        self.assertNotIn('Love stays a summer night', response.text)
        self.assertIn('405', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_valid_input_fields_and_insufficient_corresponding_search_fields(self):
        response = requests.get('/author,title/Dowson')
        self.assertIn('405', response.text)
        self.assertIn('Comma delimited fields must have corresponding semicolon delimited search terms', response.text)
        self.assertNotIn('"title":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_valid_input_fields_and_insufficient_corresponding_search_fields_return_all_output_fields_format_as_json(self):
        response = requests.get('/author,title/Dowson/all.json')
        self.assertIn('405', response.text)
        self.assertIn('Comma delimited fields must have corresponding semicolon delimited search terms', response.text)
        self.assertNotIn('"title":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_author_return_combination_of_valid_and_invalid_output_fields(self):
        response = requests.get('/author/Dowson/wrong,lines')
        self.assertNotIn('Love stays a summer night', response.text)
        self.assertIn('405', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_author_return_combination_of_valid_and_invalid_output_fields_format_as_text(self):
        response = requests.get('/author/Dowson/wrong,lines.text')
        self.assertNotIn('Love stays a summer night', response.text)
        self.assertIn('405', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_author_return_combination_of_valid_and_invalid_output_fields_format_as_invalid_format(self):
        response = requests.get('/author/Dowson/wrong,lines.bad')
        self.assertNotIn('Love stays a summer night', response.text)
        self.assertIn('405', response.text)
        self.assertEqual(response.status_code, 200)

   # TEST 405 COMBINATIONS
    def test_search_by_poemcount_and_random(self):
        response = requests.get('/poemcount,random/1;1')
        self.assertIn('405', response.text)
        self.assertIn('Use either poemcount or random as input fields, but not both.', response.text)
        self.assertNotIn('"title":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_poemcount_and_random_return_all_fields_format_as_text(self):
        response = requests.get('/poemcount,random/1;1/all.text')
        self.assertIn('405', response.text)
        self.assertIn('Use either poemcount or random as input fields, but not both.', response.text)
        self.assertNotIn('"title":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_valid_input_field_poemcount_and_random(self):
        response = requests.get('/author,poemcount,random/Dowson;1;1')
        self.assertIn('405', response.text)
        self.assertIn('Use either poemcount or random as input fields, but not both.', response.text)
        self.assertNotIn('"title":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_valid_input_field_poemcount_and_random_return_all_output_fields_format_as_json(self):
        response = requests.get('/author,poemcount,random/Dowson;1;1/title.json')
        self.assertIn('405', response.text)
        self.assertIn('Use either poemcount or random as input fields, but not both.', response.text)
        self.assertNotIn('"title":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_valid_input_fields_and_insufficient_corresponding_search_fields_return_some_output_fields_format_as_json(self):
        response = requests.get('/author,title/Dowson/title.json')
        self.assertIn('405', response.text)
        self.assertIn('Comma delimited fields must have corresponding semicolon delimited search terms', response.text)
        self.assertNotIn('"title":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_for_title_with_open_round_bracket(self):
        response = requests.get('/title/A%20Soap%20Opera%20(How')
        self.assertIn('There it was ) oh no', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)
    
    def test_search_for_lines_with_closing_round_bracket(self):
        response = requests.get('/lines/There%20it%20was%20)%20oh%20no')
        self.assertIn('There it was ) oh no', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
