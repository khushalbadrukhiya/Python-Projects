from django import template

register = template.Library()

@register.filter
def isExists(format_string,value):
    try:
        my_array = format_string.split(',')
        if str(value) in my_array:
            return True
        else:
            return False
    except:
        return False
    
@register.filter()
def str_to_int(value):
    return int(value)

@register.filter()
def twoNoAdd(no1,no2):
    return no1+no2
    
