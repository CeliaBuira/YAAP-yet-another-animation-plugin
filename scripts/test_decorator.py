
from functools import partial
from PyQt5.QtCore import QEasingCurve


def capitalized2snakecase(string):
    return "".join([("_"+i if i.isupper() else i) for i in string]).strip("_").lower()



mapping = {
 QEasingCurve.InOutCubic:"InOutCubic",
 QEasingCurve.InCubic:"InCubic"
    }


mapping = {k: capitalized2snakecase(v) for k, v in mapping.items()}





def ease_template(q_easing_curve):
    name = mapping.get(q_easing_curve, "inner")
    def ease_inner(t, parent):
        easing = QEasingCurve(q_easing_curve)
        return easing.valueForProgress(t)

    # Duck typing so everything work when turned into a qgis expression function
    ease_inner.__doc__ = """
        <h4>Syntax</h4>
        <p><b>ease_{name}</b>(  <i> t </i>)</p>
        """.format(name=name)
    ease_inner.__name__ = name
    return ease_inner

def ease_in_sin(t, parent):
    """
    <h4>Syntax</h4>
    <p><b>ease_out_sin</b>(  <i> t </i>)</p>
    """
    easing = QEasingCurve(QEasingCurve.InSine)
    return easing.valueForProgress(t)


def decorator(func):
    def wrapper(a,b):
        print("Something is happening before the function is called.")
        func(a,b)
    return wrapper

def foo(x, y):
    print(x,y)


#l = lambda
p = partial(foo, y="nobody")




foo("hello" , "world")
p("hello")

#f = decorator(ease_template(QEasingCurve.InCubic))
f = ease_template(QEasingCurve.InCubic)
f(0.2, None)

def bar(a="a", b="b"):
    print(func)
    


def decorater_a(alpha="alpha", beta="beta"):
    def wrapper(func):
        return lambda func: print("func name", func__name__)
    return wrapper

def decorater_b(func,alpha="alpha", beta="beta"):
    def wrapper():
        return lambda func : func
    return wrapper

@decorater_a(alpha="alpha", beta="beta")
def foobar():
    print("balbla")

foobar()

"""
@qgsfunction(args="auto", group="custom")
def foo():
    print("hello")
"""


"""
@qgsfunction(args="auto", group="custom")
def foo():
    print("hello")

@qgsfunction(args="auto", group="custom")
def bar():
    print("world")
qgsfunction(args="auto", group="custom")(bar)
"""



