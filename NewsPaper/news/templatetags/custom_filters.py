from django import template

# если мы не зарегистрируем наши фильтры, то Django никогда не узнает, где именно их искать и фильтры потеряются
register = template.Library()





censor_list = ['БББББ', 'ССССС', 'ХХХХХ']


@register.filter(name='censor')
def censor(value):
    for word in censor_list:
        value = value.replace(word, '*****')
    return value

# replace(word, '*****')