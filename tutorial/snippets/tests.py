from django.test import TestCase, Client
from snippets.models import *
from snippets.serializers import *
import unittest
from rest_framework.test import APITestCase, APIRequestFactory

class CategoryTestCase(unittest.TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Linguistics", imgpath="https://www.yahoo.com")

    def test_category_attributes(self):
        self.assertEqual(self.category.name, "Linguistics")
        self.assertEqual(self.category.imgpath, "https://www.yahoo.com")

class CourseTestCase(unittest.TestCase):
    def setUp(self):
        category=Category.objects.create(name='Languages')
        self.course = Course.objects.create(name="Spanish Zone", description="Миссия Spanish Zone", category=category)

    def test_course_attributes(self):
        self.assertEqual(self.course.name, "Spanish Zone")
        self.assertEqual(self.course.description, "Миссия Spanish Zone")
        self.assertEqual(self.course.logo, 'LOGO')

            #class ContactTestCase(unittest.TestCase):
            #def setUp(self):
            #category=Category.objects.create(name='Languages')
            #self.course = Course.objects.create(name="Spanish Zone", description="Миссия Spanish Zone заключается в том, чтобы помочь людям раскрыть весь их потенциал.", category=category)
            #Contact.objects.create(course=self.course, type=1, value="12345")
    


class BranchTestCase(unittest.TestCase):
    def setUp(self):
        category=Category.objects.create(name='Languages')
        self.course = Course.objects.create(name="Spanish", description="Миссия Spanish Zone заключается в том, чтобы помочь людям раскрыть весь их потенциал.", category=category)
        Branch.objects.create(
                          course=self.course,
                          latitude='latitude',
                          longitude='longitude',
                          address='address'
                          )
        
    def test_branch_attributes(self):
        branch = Branch.objects.get(course=self.course)
        self.assertEqual(branch.address, 'address')

class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_todo(self):
        response = self.client.post('/snippets/', {
                            "name": "Spanish Zone",
                            "description": "Миссия Spanish Zone заключается в том, чтобы помочь людям раскрыть весь их потенциал.",
                            "category": "Languages",
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
                            }, format='json')
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
                        "category": "Languages",
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


