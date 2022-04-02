from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Safari()

    def tearDown(self):  
        self.browser.quit()

    def test_home_page_title(self):  
        # Открытие браузера
        # Название сайта
        self.browser.get('http://localhost:8000')
        self.assertIn('Проекция', self.browser.title)  
        # self.fail('Finish the test!')  

    def test_home_page_header(self):  
        # Открытие браузера
        # Название заголовка
        self.browser.get('http://localhost:8000')
        header = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('Проекция', header)  
        # self.fail('Finish the test!') 


    def test_home_page_body(self):  
        # Открытие браузера
        # Название заголовка
        self.browser.get('http://localhost:8000')
        body = self.browser.find_element_by_class_name('body')
        self.assertTrue(body)

if __name__ == '__main__':  
    unittest.main()


    #Кадры, которые еще не опубликованный 
    
    #Кадры: открытие по короткой ссылке