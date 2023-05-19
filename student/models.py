from django.db import models
from authMain.models import AuthMain
from course.models import Course
# Create your models here.
class Student(models.Model):
    user=models.OneToOneField(AuthMain,on_delete=models.CASCADE)
    course=models.ManyToManyField(Course ,related_name='user_course')
    
    def __str__(self) -> str:
        return self.user.username