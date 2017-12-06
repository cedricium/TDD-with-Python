from selenium import webdriver
import unittest


class NewVisitorTets(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Monica has heard about a cool new online to-do app. She goes to check
        # out it's homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She types "Buy boyfriend a new MacBook Pro

        # When she hits [Enter], the page updates, and now the page lists
        # "1. Buy boyfriend a new MacBook Pro" as an item in a to-do list

        # There is still a text box inviting her to add another item. She enters
        # "Book vacation to Hawaii"

        # The page updates again, and now shows both items on her list

        # Monica wonders whether the site will remember her list. Then she sees that
        # the site has generated a unique URL for her -- there is some explanatory text
        # to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, Monica goes back to sleep


if __name__ == '__main__':
    unittest.main()
