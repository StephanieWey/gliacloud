# WEB
from flask import Flask
import random 

app = Flask(__name__)

zen_of_python = ["Beautiful is better than ugly.", "Explicit is better than implicit.", "Simple is better than complex.", "Complex is better than complicated.", "Flat is better than nested.", "Sparse is better than dense.", "Readability counts.", "Special cases aren't special enough to break the rules.", "Although practicality beats purity.", "Errors should never pass silently.", "Unless explicitly silenced.", "In the face of ambiguity, refuse the temptation to guess.", "There should be one-- and preferably only one --obvious way to do it.", "Although that way may not be obvious at first unless you're Dutch.", "Now is better than never.", "Although never is often better than *right* now.", "If the implementation is hard to explain, it's a bad idea.", "If the implementation is easy to explain, it may be a good idea.", "Namespaces are one honking great idea -- let's do more of those!"]

@app.route('/')

def random_pyzen():
    random_index = random.randint(0, len(zen_of_python)-1)
    return '{}'.format(zen_of_python[random_index])

if __name__ == '__main__':
    app.run(port=5000)
