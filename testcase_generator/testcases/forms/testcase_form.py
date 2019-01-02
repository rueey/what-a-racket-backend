from django import forms

class TestcaseForm(forms.Form):
    testcase_id = forms.CharField(label="Id of the struct", max_length=400)
    testcase_vals = forms.CharField(label="Struct representations", widget=forms.Textarea, max_length=400, required=False)
