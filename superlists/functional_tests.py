from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy boyfriend a new MacBook Pro
        inputbox.send_keys('Buy boyfriend a new MacBook Pro')

        # When she hits [Enter], the page updates, and now the page lists
        # "1. Buy boyfriend a new MacBook Pro" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy boyfriend a new MacBook Pro', [row.text for row in rows])

        # There is still a text box inviting her to add another item. She enters
        # "Book vacation to Hawaii"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Book vacation to Hawaii')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy boyfriend a new MacBook Pro', [row.text for row in rows])
        self.assertIn('2: Book vacation to Hawaii', [row.text for row in rows])

        # Monica wonders whether the site will remember her list. Then she sees that
        # the site has generated a unique URL for her -- there is some explanatory text
        # to that effect.
        self.fail('Finish the test!')

        # She visits that URL - her to-do list is still there.

        # Satisfied, Monica goes back to sleep


if __name__ == '__main__':
    unittest.main()
