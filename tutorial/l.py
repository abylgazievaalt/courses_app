from snippets.models import *
from snippets.serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

course = Course.objects.create(name='Python for everyone', description='University of Michigan')
Branch.objects.create(course=course, latitude='12.34', longtitude='34.56', address='Aaly Tokombaev, 45')
serializer = CourseSerializer(instance=course)
serializer.data
