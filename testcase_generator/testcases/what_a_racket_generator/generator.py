import random, math

#Stuff for primitives
alphabet = ['#\\'+chr(ord('a')+i) for i in range(26)]
special_chars = ["#\\newline", "#\\space"]
digits = ['#\\' + str(i) for i in range(10)]

chars = alphabet + special_chars + digits

"""
This code will be the overall generator for primitive data types in racket:
    Numbers
    Decimal Numbers (lol)
    Booleans
    Strings
    Characters
    Lists
"""


def generate_bool():
    return [True, False][random.randint(0, 1)]


def generate_num(min_val=-99999, max_val=99999):
    return random.randint(min_val, max_val)


def generate_float(min_val=-99999, max_val=99999):
    decimal = random.random()
    return random.randrange(min_val, math.floor(max_val-decimal))+decimal


def generate_char():
    """
    For the sake of readability and convenience, generate_char will only do alphanumeric and whitespace
    characters in racket
    """
    return random.choice(chars)


def generate_string(length=5):
    return '"' + (''.join(generate_char() for i in range(length))) + '"'


funcs = {'Bool': generate_bool, 'Num': generate_num, 'Float':generate_float,
         'Char':generate_char, 'Str':generate_string, 'Nat':lambda : generate_num(0, 99999999)}

any = ('Bool', 'Num', 'Float', 'Char', 'Str', 'Nat')


def generate_primitive(types=any):
    return funcs[random.choice(types)]()


#The next portion will handle the recursive structs of racket
#it will handle it using the format (listof primitives) (listof structs)

def generate_list_primitives(types=any, size=5):
    """
    sample generator for a struct, specifically list
    NOTE: IT DOESN'T TAKE STRUCTS
    :param types: types of parameters allowed
    :param size: the length of the list
    :return: a randomized list
    """
    cval = funcs[random.choice(types)]()
    if size == 0:
        return None
    elif size == 1:
        return [cval]
    else:
        subcase = generate_list_primitives(types, size-1)
        subcase.append(cval)
        return subcase


class Struct:
    def __init__(self, id, vals):
        """
        a representation of necessary information to generate Racket structs
        :param vals: all the names of the possible values is a (listof (listof Str))
        """
        self.id = id
        self.base_vals = [list(filter(lambda x: x in primitives, val)) for val in vals]
        self.vals = vals

class Item:
    """
    class that stores each item of a struct, holding the substruct size
    the struct_id will be the name of the struct of the current item
    the sub_struct will either be another Item or a primitive or None
    """
    def __init__(self, struct_id, sub_struct):
        self.struct_id = struct_id
        self.sub_struct = sub_struct
        if(not (type(self.sub_struct) is list)):
            self.sub_struct = [self.sub_struct]

    def __str__(self):
        return self.struct_id + ": [" + str(self.sub_struct) + "]"

#Stuff for structs
#struct_id:struct
primitives = ('Bool', 'Num', 'Float', 'Char', 'Str', 'Nat', 'empty')
struct_list = {val: Struct(val, list(list(val))) for val in primitives}
struct_list["Posn"] = Struct("Posn", (('Num', 'Nat'), ('Num', 'Nat')))

def generate_struct(struct_name, depth):
    """
    recursively generates a struct with a specified max depth
    only provides strings, no actual random values
    :param struct_name: name of current level data type
    :param depth: current depth
    :return: a struct.
    """
    if depth == 0:
        ret = [random.choice(base) for base in struct_list[struct_name].base_vals]
        return ret
    else:
        ret = []
        for val in struct_list[struct_name].vals:
            curr_type = random.choice(val)

            if curr_type in primitives:
                ret += [curr_type]
            else:
                ret += [Item(curr_type, generate_struct(curr_type, depth-1))]
        end = Item(struct_name, ret)
        return end

def print_struct(struct):
    """
    prints a specified struct
    :param struct: an Item
    :return: None
    """
    if isinstance(struct, str):
        #assume is a primitive for now
        return funcs[struct]()
    else:
        #is of type Item, check subtype
        ret = "( make-"+struct.struct_id
        for subitem in struct.sub_struct:
            ret += " " + print_struct(subitem)
        ret += " )"
        return ret

#struct_list["binode"] = Struct("binode", (("binode", "Str"), ("binode", "Str")))

#print(print_struct(generate_struct("binode", 3)))
