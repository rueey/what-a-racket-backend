from django.db import models

def parse_values(val_string, token):
    return val_string.split(token)

class ValuesField(models.Field):
    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super(ValuesField, self).__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if(not value):
            return None
        return parse_values(value, self.token)

    def to_python(self, value):
        if(isinstance(value, list)):
            return value
        if(not value):
            return None
        return parse_values(value, self.token)

    def get_prep_value(self, value):
        return self.token.join([unicode(str) for str in value])
