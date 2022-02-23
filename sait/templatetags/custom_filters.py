from django import template

register = template.Library()  # если мы не зарегистрируем наши фильтры, то Django никогда не узнает, где именно их искать, и фильтры потеряются

@register.filter(name='multiply')  # регистрируем наш фильтр под именем multiply, чтоб django понимал, что это именно фильтр, а не простая функция
def multiply(value, arg):  # первый аргумент здесь — это то значение, к которому надо применить фильтр, второй аргумент — это аргумент фильтра, т. е. примерно следующее будет в шаблоне value|multiply:arg
    return str(value) * arg  # возвращаемое функцией значение — это то значение, которое подставится к нам в шаблон


@register.filter(name='censor')
def censor(value):
    if isinstance(value, str):
        list = ['ух', 'ор', 'ах', 'ай', 'бля', 'сука', 'хуй', 'дебил', ] # Список нецензурных слов
        for A in list:
            value = value.replace(A, '#') # Замена совпадений подстроки на @!#%
        return str(value)
    else:
        raise ValueError(f'Нельзя преобразовать {type(value)}')

"""@register.filter(name='censor')
def censor(value):
    cens_words = ['word1', 'word2'] #'сука', 'бля', 'блять', 'блядь', 'пиздец', 'пизда', 'хуй', 'нахуй']
    text = set(value.split())
    for i in text:
        for j in cens_words:
            if i == j:
                return value.replace(i, '*' * len(i))
            return value"""

"""@register.filter(name='censor')
def censor(value):
    list_of_bad_words = ['suka', 'blyat', 'debil', 'blya', 'pizdec']
    for bad_word in list_of_bad_words:
        while True:
            if bad_word in value:
                value = value.replace(bad_word, '*' * len(bad_word))
            else:
                break
    return value"""

"""#    text = set(value.split())
#    for i in text:
#        for j in cens_words:
#            if i == j:
#                return value.replace(i, '*' * len(i))
#    return value"""