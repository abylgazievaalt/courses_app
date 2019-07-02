from snippets.models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('address', 'latitude', 'longitude')

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('type', 'value')

class CourseSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)
    branches = BranchSerializer(many=True, required=False)
    contacts = ContactSerializer(many=True, required=False)

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'category',
                  'logo', 'contacts', 'branches']

    def create(self, validated_data):
        #categories_list = []
        #branches_list = []
        #contacts_list = []
        branches_data = validated_data.pop('branches')
        contacts_data = validated_data.pop('contacts')
        course = Course.objects.create(**validated_data)
        for branch_data in branches_data:
        #   branches_list.append(Branch.objects.create(course=course, **branch_data))
            Branch.objects.create(course=course, **branch_data)
        for contact_data in contacts_data:
        #   contacts_list.append(Contact.objects.create(course=course, **contact_data))
            Contact.objects.create(course=course, **contact_data)
        course.save()
        return course
