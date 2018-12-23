from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("At index")

def edit_testcase(request, testcase_id):
    return HttpResponse("Editing testcase %s" % testcase_id)

def testcase_list(request):
    return HttpResponse("Displaying list of testcases")
