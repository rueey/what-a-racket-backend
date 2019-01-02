from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import Testcase
from .forms.testcase_form import TestcaseForm
from . import utils

# Create your views here.

def index(request):
    return render(request, 'testcase_detail.html', {'testcase_form': TestcaseForm()})

def testcase_detail(request, testcase_id):
    t = get_object_or_404(Testcase, pk=testcase_id)
    form = TestcaseForm(initial={'testcase_id': t.testcase_id, 'testcase_vals': t.testcase_vals})
    return render(request, 'testcase_detail.html', {'testcase': t, 'testcase_form': form})

def create_testcase(request):
    error = None
    if(request.method == 'POST'):
        form  = TestcaseForm(request.POST)
        if form.is_valid():
            try:
                t = Testcase(testcase_id=form.cleaned_data['testcase_id'],
                        testcase_vals=form.cleaned_data['testcase_vals'],
                        generated_text=utils.create_testcase(form.cleaned_data['testcase_id'], form.cleaned_data['testcase_vals']),
                        pub_date = timezone.now())
                t.save()
                return HttpResponseRedirect(reverse('testcases:testcase_detail', args=(t.id,)))
            except:
                error = "Incorrect specifications"
    else:
        form = TestcaseForm()
    return render(request, 'testcase_detail.html', {'testcase_form': form, 'error': error})


def edit_testcase(request, testcase_id):
    t = get_object_or_404(Testcase, pk=testcase_id)
    error = None
    if(request.method == 'POST'):
        form  = TestcaseForm(request.POST)
        if form.is_valid():
            try:
                t.testcase_id = form.cleaned_data['testcase_id']
                t.testcase_vals = form.cleaned_data['testcase_vals']
                t.generated_text = utils.create_testcase(t.testcase_id, t.testcase_vals)
                t.pub_date = timezone.now()
                t.save()
                return HttpResponseRedirect(reverse('testcases:testcase_detail', args=(t.id,)))
            except:
                error = "Incorrect specifications"
    else:
        form = TestcaseForm(initial={'testcase_id': t.testcase_id, 'testcase_vals': t.testcase_vals})
    return render(request, 'testcase_detail.html', {'testcase': t, 'testcase_form': form, 'error': error})

