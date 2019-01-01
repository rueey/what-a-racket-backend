from django import forms

class TestcaseForm(forms.Form):
    name = forms.CharField(label="Name of testcase", max_length=50)
    testcase_id = forms.CharField(label="Ids of the structs", max_length=400)
    testcase_vals = forms.CharField(label="Struct representation", max_length=400)
