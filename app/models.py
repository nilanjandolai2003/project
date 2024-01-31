from django.db import models



# Create your models here.

class department(models.Model):
    name=models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.name
class Role(models.Model):
    name=models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.name
class student(models.Model):
    first_name=models.CharField(max_length=100,null=False)
    last_name=models.CharField(max_length=100)
    department=models.ForeignKey(department,on_delete=models.CASCADE)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    phone=models.IntegerField()
    join_date=models.DateTimeField()
    id = models.CharField(max_length=20,unique=True, editable=False,primary_key=True)

     
    def __str__(self):
        return "%s %s  "%(self.first_name,self.last_name)