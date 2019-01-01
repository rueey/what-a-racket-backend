from .what_a_racket_generator import generator
from .models import Testcase
from .forms.testcase_form import TestcaseForm

def parse_testcase_spec_string(specs):
    mod_str = specs.strip('()')
    br = 0
    running_str = ""
    tokens = []
    for c in mod_str:
        if(c == ' ' and br == 0):
            tokens.append(running_str)
            running_str = ""
        else:
            if(c == '('):
                br += 1
            elif(c == ')'):
                br -= 1
            running_str += c
    if running_str:
        tokens.append(running_str)
    ret = []
    print(tokens, br, running_str)
    for token in tokens:
        if(token.startswith('(')):
            ret.append(parse_testcase_spec_string(token))
        else:
            ret.append(token)
    return ret

def create_testcase(specification):
    specs = parse_testcase_spec_string(specification)
    return specs

def deserialize_specs(specs):
    pass

def save_testcase(n, t_id, t_vals):
    t = Testcase(name=n, testcase_id=t_id, testcase_vals=t_vals)
    t.save()

if __name__ == "__main__":
    print(create_testcase("(make-x Num (make-y (make-z Str Num) Int) Int)"))

