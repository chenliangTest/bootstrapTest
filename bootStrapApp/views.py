from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import RequestContext
from django.core import serializers
# from bootStrapApp.entity import emp
# from bootStrapApp.models import Emps
from django.http import HttpResponse
from bootStrapApp.model.EmpsModel import Empss
from bootStrapApp.entity.empsEntity import EmpsInfo
from bootStrapApp.forms.EmpsForms import EmpsForm
from django.views.decorators.csrf import csrf_exempt
import json


# 初始化页面
def loginfo(request):
	return render(request, 'init.html')


# 登录后主页
def homepage(request):
	# 传统数据库连接操作数据库
	# cursor = db.database()
	# sql = 'select * from emps'
	# cursor.execute(sql)
	# rows = cursor.fetchall()
	# empsList = []
	# for i in range(len(rows)):
	# 	convert = emp.Emp(rows[i])
	# 	empsList.append(convert)
	
	# 通过操作数据模型操作数据库
	rows = Empss.objects.all()
	return render(request, 'homepage.html', {'emps': rows})


# 获取员工信息列表
def getEmpsInfoList(request):
	rows = Empss.objects.all()
	# Emps.objects.all()
	# print(rows)
	return render(request, 'empList.html', {'emps': rows})


# 获取员工信息列表
def selectEmpsInfo(request):
	# ename = request.GET['ename']
	# rows = Empss.objects.all()
	# return render(request, 'empList.html', {'emps': rows})
	rows = Empss.objects.all()
	_json = serializers.serialize("json", rows)
	print(_json)
	return HttpResponse(_json)


# 新增初始化页面
def insertInit(request):
	# 传统数据库连接操作数据库
	# cursor = db.database()
	# sql = 'select * from emps'
	# cursor.execute(sql)
	# rows = cursor.fetchall()
	# empsList = []
	# for i in range(len(rows)):
	# 	convert = emp.Emp(rows[i])
	# 	empsList.append(convert)
	
	# 通过操作数据模型操作数据库
	# rows = Empss.objects.all()
	# _json = serializers.serialize("json", rows)
	# print(_json)
	# return HttpResponse(_json)
	
	return render_to_response('addEmpsInfo.html')

@csrf_exempt
def insertEmpsInfo(request):
	# print(request.POST)
	data = request.POST['data']
	data = data.replace("&", ",")
	data = data.replace("=", ":")
	# data = serializers.serialize("json", data)
	# print(request.POST)
	form = EmpsForm(request.POST)
	if form.is_valid():
		form.save()
	else:
		print(form)
	return render_to_response('addEmpsInfo.html')

def deleteInit(request):
	rows = Empss.objects.all()
	# Emps.objects.all()
	# print(rows)
	return render(request, 'delEmpsInfo.html', {'emps': rows})

def delEmpsInfo(request) :
	empno = request.GET['empno']
	d = Empss.objects.get(empno=empno)
	d.delete()
	
	rows = Empss.objects.all()
	return render(request, 'delEmpsInfo.html', {'emps': rows})