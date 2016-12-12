#!/usr/bin/env python
# coding: utf-8
from django import forms


def run():
	print("hello")


if __name__ == "__main__":
	run()


class EmpsInfo(forms.Form):
	empno = forms.CharField(max_length=10)
	ename = forms.CharField(max_length=10)
	job = forms.CharField(max_length=9)
	mgr = forms.CharField(max_length=10)
	hiredate = forms.CharField(max_length=20)
	sal = forms.CharField(max_length=10)
	comm = forms.CharField(max_length=10)
	deptno = forms.CharField(max_length=10)
