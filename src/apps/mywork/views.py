# coding: utf-8
from django.shortcuts import render

from django.views.generic.base import View

__author__ = 'dyp'


class SalaryCheckPage(View):
    """
    薪资核算页面
    """

    @staticmethod
    def get(request):
        return render(request, 'mywork/salarycheck.html', {})
