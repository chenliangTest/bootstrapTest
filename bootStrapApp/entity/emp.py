#!/usr/bin/env python
# coding: utf-8

def run():
	print("hello")


if __name__ == "__main__":
	run()
	
	
class Emp(object):
	def __init__(self, object):
		self.empno = object[0]
		self.ename = object[1]
		self.job = object[2]
		self.mgr = object[3]
		self.hiredate = object[4]
		self.sal = object[5]
		self.comm = object[6]
		self.deptno = object[7]
		
	def __repr__(self):
		print(self.empno,self.empno,self.job,self.mgr,self.hiredate,self.comm,self.deptno)
