#!/usr/bin/env python
# coding: utf-8
from django.db import models


def run():
	print("hello")


if __name__ == "__main__":
	run()


# Create your model here.
class Empss(models.Model):
	empno = models.BigIntegerField(max_length=10, primary_key=True)
	ename = models.CharField(max_length=10)
	job = models.CharField(max_length=9)
	mgr = models.BigIntegerField(max_length=10)
	hiredate = models.CharField(max_length=20)
	sal = models.BigIntegerField(max_length=10)
	comm = models.BigIntegerField(max_length=10)
	deptno = models.BigIntegerField(max_length=10)
	
	class Meta:
		db_table = 'emps'
	
	def __unicode__(self):
		return self.empno, self.ename
