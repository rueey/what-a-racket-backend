from .what_a_racket_generator import generator

def parse_testcase_spec_string(specs):
    mod_str = specs.split('\n')
    br = 0
    tokens = []
    for s in mod_str:
        s = s.strip('()')
        running_str = ""
        struct = []
        for c in s:
            if(c == ' ' and br == 0):
                struct.append(running_str)
                running_str = ""
            else:
                if(c == '('):
                    br += 1
                elif(c == ')'):
                    br -= 1
                running_str += c
        if running_str:
            struct.append(running_str)
        tokens.append(struct)
    ret = {}
    for token in tokens:
        if(len(token) == 3 and token[0].startswith('make-')):
            ret[token[0][5:]] = ((token[0][5:], token[1]), (token[0][5:], token[2]))
        else:
            raise ValueError("Incorrect specifications")
    return ret

def create_testcase(struct_id, specification):
    specs = parse_testcase_spec_string(specification)
    for key, value in specs.items():
        print(value)
        generator.struct_list[key] = generator.Struct(key, value)
    ret = generator.generate_struct(struct_id, 3)
    print(ret)
    return ret
