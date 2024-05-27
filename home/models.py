from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=1000)
    def __str__(self):
        return self.title


class Test(models.Model):
    STATUS = (
        ("True", "Mavjud"),
        ('False', 'Mavjud emas'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    questions = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/Test',
    validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', ])], blank=True, null=True,)
    status = models.CharField(max_length=15, choices=STATUS, default='False', verbose_name='Status')
    answer = RichTextUploadingField()
    def __str__(self):
        return self.questions

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return (f'{self.user.username}')