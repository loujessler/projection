from urllib import response
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from framesearch.models import Frame
from datetime import datetime

from framesearch.views import home_page  

class HomePageTest(TestCase):

    def test_home_page_displays_frame(self):
        Frame.objects.create(
            title = 'title 1',
            summary = 'summary 1',
            category = 'category 1',
            pubdate = datetime.now(),
            full_text = 'full_text 1',
        )
        Frame.objects.create(
            title = 'title 2',
            summary = 'summary 2',
            category = 'category 2',
            pubdate = datetime.now(),
            full_text = 'full_text 2',
        )

        request = HttpRequest()  
        response = home_page(request)
        html = response.content.decode('utf8')  
 
        self.assertIn('title 1', html)  
        self.assertIn('summary 1', html)
        self.assertNotIn('full_text 1', html)

        self.assertIn('title 2', html)  
        self.assertIn('summary 2', html)
        self.assertNotIn('full_text 2', html)

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, home_page)  

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = home_page(request)  
        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))  
        self.assertIn('<title>Проекция</title>', html)  
        self.assertIn('<h1>Проекция</h1>', html)  
        self.assertTrue(html.endswith('</html>'))

class FrameModelTest(TestCase):

    def test_frame_model_save_and_retrieve(self):
        # Создать кадр 1
        # сохранить кадр в базе
        frame1 = Frame(
            title = 'frame 1',
            full_text = 'full_text 1',
            summary = 'summary 1',
            category = 'category 1',
            pubdate = datetime.now(),
        )
        frame1.save()


        # создать кадр 2
        # сохранить кадр 2 в базе
        frame2 = Frame(
            title = 'frame 2',
            full_text = 'full_text 2',
            summary = 'summary 2',
            category = 'category 2',
            pubdate = datetime.now(),
        )
        frame2.save()


        # загрузить из базы все кадры
        all_frame = Frame.objects.all()
        # проверить кол-во кадров
        self.assertEqual(len(all_frame), 2)
        # проверить 1 кадр из базы == кадр 1
        self.assertEqual(
            all_frame[0].title,
            frame1.title
        )
        # проверить 2 кадр из базы == кадр 2
        self.assertEqual(
            all_frame[1].title,
            frame2.title
        )