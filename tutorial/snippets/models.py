from django.db import models

class Category(models.Model):

    name = models.IntegerField()
    imgpath = models.CharField(max_length=100, blank=True, default='')
    
    def __str__(self):
        return '%s' % (self.name)

class Branch(models.Model):

    course = models.ForeignKey('Course', related_name='branches', on_delete=models.CASCADE, null=True)
    latitude = models.CharField(max_length=100, blank=True, default='')
    longitude = models.CharField(max_length=100, blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return '%s, %s, %s, %s' % ( self.address, self.latitude, self.longitude)

class Contact(models.Model):
    course = models.ForeignKey('Course', related_name='contacts', on_delete=models.CASCADE, null=True)
    phone = 1
    facebook = 2
    email = 3
    CONTACT_CHOICES = [(phone, "PHONE"),(facebook, "FACEBOOK"),(email, "EMAIL")
        ]
    type = models.CharField(max_length=10, choices=CONTACT_CHOICES, default='')
    value = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return '%s, %s' % (self.type, self.value)

class Course(models.Model):

    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=300, blank=True, default='')
    logo = models.CharField(max_length=300, blank=True, default='LOGO')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return str(self.name)
