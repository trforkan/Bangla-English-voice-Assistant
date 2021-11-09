
from googletrans import *


def transb(query):
    translator = Translator()
    result = translator.translate(query, src='bn', dest='en')
    query=result.text

    # print(result.src)
    # print(result.dest)
    # print(query)
    return query


def transe(query):
    translator = Translator()
    result = translator.translate(query, src='en', dest='bn')
    query=result.text

    # print(result.src)
    # print(result.dest)
    # print(query)
    return query