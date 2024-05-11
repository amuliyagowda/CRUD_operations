from django.shortcuts import render

# Create your views here.
from app.models import *



def equijoins(request):
    JDED=Emp.objects.select_related('deptno').all()
    JDED=Emp.objects.select_related('deptno').filter(ename='SMITH')
    JDED=Emp.objects.select_related('deptno').filter(comm__contains=0)
    JDED=Emp.objects.select_related('deptno').filter(ename__startswith='S')
    JDED=Emp.objects.select_related('deptno').filter(hiredate__month=5)
    JDED=Emp.objects.select_related('deptno').filter(salary__gt=1000)

    d={'JDED':JDED}
    return render(request,'equijoins.html',d)

def selfjoins(request):
    JMED=Emp.objects.select_related('mgr').all()
    JMED=Emp.objects.select_related('mgr').filter(ename__contains='S')
    #JMED=Emp.objects.select_related('mgr').filter(mgr__manager no__isnull=True)
    JMED=Emp.objects.select_related('mgr').filter(salary__gt=5000)
    JMED=Emp.objects.select_related('mgr').filter(ename='MARTIN')
    #JMED=Emp.objects.select_related('mgr').filter(managerno=4444)
    JMED=Emp.objects.select_related('mgr').filter(ename='MARTIN',salary=7654)
    JMED=Emp.objects.select_related('mgr').filter(mgr=4444)
    d={'JMED':JMED}
    return render(request,'selfjoins.html',d)

def empdeptmgr(request):
    EDMJD=Emp.objects.select_related('deptno','mgr').all()
    EDMJD=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=False)
    EDMJD=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='SMITH')
    EDMJD=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='ALLEN',deptno__dname__startswith='S')
    EDMJD=Emp.objects.select_related('deptno','mgr').filter(job__startswith='C',job__contains='R')
    EDMJD=Emp.objects.select_related('deptno','mgr').filter(job__endswith='MAN')
    EDMJD=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='SMITH',deptno__dname__contains='S')
    EDMJD=Emp.objects.select_related('deptno','mgr').filter(salary__lt=2000)
    EDMJD=Emp.objects.select_related('deptno','mgr').filter(mgr__salary__gt=2000)
    EDMJD=Emp.objects.extra(where=['LENGTH(ename) = 5'])
    EDMJD=Emp.objects.extra(where=[" ename like'%TH' "])
    EDMJD=Emp.objects.extra(where=["job like'%MAN' "])
    EDMJD=Emp.objects.extra(where=[" ename like 'S%' "])
    d={'EDMJD':EDMJD}
    return render(request,'empdeptmgr.html',d)

def updateemp(request):
    Emp.objects.filter(ename='kushi').update(job='RESEARCH')
    Emp.objects.filter(job='CLERK').update(salary=2000)
    Emp.objects.filter(ename='ALLEN').update(deptno=10)
    Emp.objects.update_or_create(ename='hema', defaults={'salary':1000})
    Emp.objects.update_or_create(ename='MARTIN', defaults={'job':'SALESMAN'})
    DO=Dept.objects.get(deptno=10)
    Emp.objects.update_or_create(job='SALESMAN', defaults={'deptno':DO})
    UEDMD=Emp.objects.select_related('deptno','mgr').all()
    d={'UEDMD':UEDMD}
    return render(request,'updateemp.html',d)

def delete_emp(request):
    Emp.objects.filter(job='ANALYST').delete()
    Dept.objects.filter(deptno=30).delete()
    Dept.objects.all().delete()
    DEMDO =Emp.objects.select_related().all()
    d={'DEMDO':DEMDO}
    return render(request,'delete_emp.html',d)