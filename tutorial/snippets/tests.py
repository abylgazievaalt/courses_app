from django.test import TestCase, Client
from snippets.models import *
from snippets.serializers import *
import unittest
from rest_framework.test import APITestCase, APIRequestFactory

class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_create_todo(self):
        response = self.client.post('/snippets/', {
                                    "name": "Spanish Zone",
                                    "description": "Миссия Spanish Zone заключается в том, чтобы помочь людям раскрыть весь их потенциал.",
                                    "category": 4,
                                    "logo": "http://www.answersfrom.com/wp-content/uploads/2011/09/Not-talanted-but-curious.jpg",
                                    "contacts": [
                                                 {
                                                 "type": 1,
                                                 "value": "0770 792 299"
                                                 },
                                                 {
                                                 "type": 2,
                                                 "value": "https://www.facebook.com/english.zone.kg/"
                                                 },
                                                 {
                                                 "type": 3,
                                                 "value": "ezone.kg@gmail.com"
                                                 }
                                                 ],
                                    "branches": [
                                                 {
                                                 "address": "Manas 58/ Aini - right next to the Manas university",
                                                 "latitude": "42.847971",
                                                 "longitude": "74.586733"
                                                 },
                                                 {
                                                 "address": "Бишкек, Юг-2 дом 15а Советская/Горького",
                                                 "latitude": "42.8586017",
                                                 "longitude": "74.6068425"
                                                 }
                                                 ]
                                    })
        self.assertEqual(response.status_code, 201)
    
    def test_details(self):
        response = self.client.get('/snippets/78/')
        self.assertEqual(response.status_code, 200)
    
    def test_not_found(self):
        response = self.client.get('/snippets/1/')
        self.assertEqual(response.status_code, 404)

    def test_invalid_get_request(self):
        response = self.client.get('/78/')
        self.assertEqual(response.status_code, 404)

    def test_invalid_post_request(self):
        response = self.client.post('/snippets/', {
                            "name": "Spanish Zone",
                            "description": "Миссия Spanish Zone заключается в том, чтобы помочь людям раскрыть весь их потенциал.",
                            "category": 4,
                            "logo": "http://www.answersfrom.com/wp-content/uploads/2011/09/Not-talanted-but-curious.jpg",
                            "contact": [
                                         {
                                         "type": 1,
                                         "value": "0770 792 299"
                                         },
                                         {
                                         "type": 2,
                                         "value": "https://www.facebook.com/english.zone.kg/"
                                         },
                                         {
                                         "type": 3,
                                         "value": "ezone.kg@gmail.com"
                                         }
                                         ],
                            "branch": [
                                         {
                                         "address": "Manas 58/ Aini - right next to the Manas university",
                                         "latitude": "42.847971",
                                         "longitude": "74.586733"
                                         },
                                         {
                                         "address": "Бишкек, Юг-2 дом 15а Советская/Горького",
                                         "latitude": "42.8586017",
                                         "longitude": "74.6068425"
                                         }
                                         ]
                                })
        self.assertEqual(response.status_code, 400)

    def test_list_courses(self):
        response = self.client.get('/snippets/')
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)


