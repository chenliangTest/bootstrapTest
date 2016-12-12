#!/usr/bin/env python
# coding: utf-8
import cx_Oracle
from django.db import connection


def run():
	print("hello")


if __name__ == "__main__":
	run()


def database():
	conn = cx_Oracle.connect('scott/root@orcl')
	cursor = conn.cursor()
	# cursor = connection.cursor()
	return cursor