import unittest
import requests


class TestPoetryDb(unittest.TestCase):
    def test_home_page(self):
        response = requests.get('http://localhost:3000/')
        self.assertIn('PoetryDB is the world\'s first API for next generation internet poets', response.text)
        self.assertEqual(response.status_code, 200)

    # TC: Response 200 for the following endpoints (/author, /authors, /author/:authorName)
    def test_author_search(self):
        response = requests.get('http://localhost:3000/author')
        self.assertIn('Ernest Dowson', response.text)
        self.assertIn('Emily Dickinson', response.text)
        self.assertEqual(response.status_code, 200)

        response = requests.get('http://localhost:3000/authors')
        self.assertIn('Ernest Dowson', response.text)
        self.assertIn('Emily Dickinson', response.text)
        self.assertEqual(response.status_code, 200)

        response = requests.get('http://localhost:3000/author/Dowson')
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    # TC: Response 200 for the following endpoints (/title, /titles, /titles/:titleName)
    def test_list_all_titles_method_1(self):
        response = requests.get('http://localhost:3000/title')
        self.assertIn('Bereavement in their death to feel', response.text)
        self.assertIn('Said Death to Passion', response.text)
        self.assertIn('The Moon Maiden\'s Song', response.text)
        self.assertEqual(response.status_code, 200)

    def test_list_all_titles_method_2(self):
        response = requests.get('http://localhost:3000/titles')
        self.assertIn('Bereavement in their death to feel', response.text)
        self.assertIn('Said Death to Passion', response.text)
        self.assertIn('The Moon Maiden\'s Song', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_title(self):
        response = requests.get("http://localhost:3000/title/The%20Moon%20Maiden's%20Song")
        self.assertIn('Love stays a summer night', response.text)
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertNotIn('Bereavement in their death to feel', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    # TC: Response 200 for the following endpoints (/random)
    def test_find_random_poem(self):
        response = requests.get('http://localhost:3000/random/1')
        self.assertNotIn('},', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_find_random_poem_return_format_as_text(self):
        response = requests.get('http://localhost:3000/random/1/title,lines,author.text')
        self.assertNotIn('},', response.text)
        self.assertIn("title\n", response.text)
        self.assertIn("author\n", response.text)
        self.assertIn("lines\n", response.text)
        self.assertNotIn("linecount\n", response.text)
        self.assertEqual(response.status_code, 200)

    # TC: Response 200 for searching poems
    def test_search_by_author_title(self):
        response = requests.get('http://localhost:3000/author,title/Dickinson;Said%20Death%20to%20Passion')
        self.assertIn('And the Debate was done.', response.text)
        self.assertIn('"title":', response.text)
        self.assertIn('"author":', response.text)
        self.assertIn('"lines":', response.text)
        self.assertIn('"linecount":', response.text)
        self.assertEqual(response.status_code, 200)

    #TC: Response 404 - No matches found
    def test_search_by_author_linecount_no_linecount_matches(self):
        response = requests.get('http://localhost:3000/author,linecount/Dowson;6/title,lines,linecount')
        self.assertNotIn('Love stays a summer night', response.text)
        self.assertIn('404', response.text)
        self.assertIn('Not found', response.text)
        self.assertEqual(response.status_code, 200)
    
    def test_search_by_author_title_exactly_when_no_title_matches(self):
        response = requests.get('http://localhost:3000/author,title/Dickinson;Said:abs')
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertIn('404', response.text)
        self.assertIn('Not found', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_author_exactly_title_no_author_matches(self):
        response = requests.get('http://localhost:3000/author,title/Dickinson:abs;Said%20Death%20to%20Passion:abs')
        self.assertNotIn('And the Debate was done.', response.text)
        self.assertIn('404', response.text)
        self.assertIn('Not found', response.text)
        self.assertEqual(response.status_code, 200)

     # TC: Response 405 - Invalid Format
    def test_search_by_author_invalid_format_1(self):
        response = requests.get('http://localhost:3000/author/Dowson/title,lines,author.wrong')
        self.assertNotIn('Love stays a summer night', response.text)
        self.assertIn('405', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_author_invalid_format_2(self):
        response = requests.get('http://localhost:3000/author/Dowson/all.wrong')
        self.assertNotIn('Love stays a summer night', response.text)
        self.assertIn('405', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_valid_input_fields_and_insufficient_corresponding_search_fields(self):
        response = requests.get('http://localhost:3000/author,title/Dowson')
        self.assertIn('405', response.text)
        self.assertIn('Comma delimited fields must have corresponding semicolon delimited search terms', response.text)
        self.assertNotIn('"title":', response.text)
        self.assertEqual(response.status_code, 200)

    def test_search_by_author_return_combination_of_valid_and_invalid_output_fields(self):
        response = requests.get('http://localhost:3000/author/Dowson/wrong,lines')
        self.assertNotIn('Love stays a summer night', response.text)
        self.assertIn('405', response.text)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()

