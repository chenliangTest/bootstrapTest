#!/usr/bin/env python
# coding: utf-8
from django.forms import ModelForm
from bootStrapApp.model.EmpsModel import Empss


def run():
	print("hello")


if __name__ == "__main__":
	run()


class EmpsForm(ModelForm):
	class Meta:
		model = Empss
		fields = '__all__'  # 选择model中所有字段为表单中的字段
	# ['empno', 'ename', 'job', 'mgr','hiredate','sal','comm','deptno']
