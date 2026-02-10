from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class works(models.Model):
    title = models.CharField("學習歷程檔案名稱",max_length=15)#標題
    desc = models.TextField("說明")#說明文
    jpg = models.FileField(upload_to='jpg/',null=True, blank=True)#上傳檔案
    classes_id = models.IntegerField("課程編號編號")#任課
    created_date = models.DateField("建立日期",auto_now_add = True)#自動填寫時間
    Certification = models.BooleanField("是否需要認證",default = False)#認證 T?F?
    topic_id = models.IntegerField("上傳區域編號")#屬於哪個主題

    def __str__(self): 
        return "{}-{}".format(self.title,self.created_date)

class updateoption(models.Model):
    topic = models.CharField("上傳區域名稱",max_length=15)#上傳類別eg.多元學習、學習成果、競賽經歷
    introduce = models.TextField("說明")#簡介類別的小文字
    amount = models.IntegerField("檔案數",default = 0)#目前擁有的檔案數

    def __str__(self): 
        return "{}".format(self.topic)
    
class classes(models.Model):
    course_name = models.CharField("課程名稱",max_length=15)#上傳認證的課程的名稱
    teacher = models.CharField("授課老師",max_length=5)#授課老師
    course_startdate = models.DateField("授課開始日期",null=True, blank=True)#授課開始時間
    course_enddate = models.DateField("授課結束日期",null=True, blank=True)#授課結束時間


    def __str__(self): 
        return "{}-{}-{}-{}".format(self.course_name,self.teacher,self.course_startdate,self.course_enddate)
    
class User(AbstractUser):
    
    ROLE_CHOICES = (
        ('teacher', '老師'),
        ('student', '學生'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"