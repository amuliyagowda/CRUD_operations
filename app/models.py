from django.db import models

# Create your models here.

class  Dept(models.Model):
    deptno=models.PositiveIntegerField(primary_key=True)
    dname=models.CharField(max_length=100,unique=True)
    location=models.CharField(max_length=100)

    def __str__(self):
        return str(self.deptno)

class Emp(models.Model):
    empno=models.PositiveIntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100,null=True)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    hiredate=models.DateField(null=True)
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    comm=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.empno)
    

class Salgrade(models.Model):
    grade=models.PositiveIntegerField(primary_key=True)
    losal=models.DecimalField(max_digits=10,decimal_places=2)
    hisal=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return str(self.grade)

