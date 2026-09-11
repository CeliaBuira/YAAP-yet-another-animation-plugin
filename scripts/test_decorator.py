
from functools import partial
from qgis.PyQt.QtCore import QEasingCurve



def capitalized2snakecase(string):
    return "".join([("_"+i if i.isupper() else i) for i in string]).strip("_").lower()


"""
for i in QEasingCurve.Type:
    keep = False
    name = i.name
    if name.startswith("In"):
        keep = True
    if name.startswith("Out"):
        keep = True
    if name.startswith("InOut"):
        keep = True
    if name.startswith("OutIn"):
        keep = True
        
    if name == "InCurve" or name == "OutCurve":
        #legacy of Qt we don't care
        keep = False
    
    if keep:
        print(f'QEasingCurve.Type.{name}: "{name}",')        
"""

#Generate with code above 
mapping = {
    QEasingCurve.Type.InQuad: "InQuad",
    QEasingCurve.Type.OutQuad: "OutQuad",
    QEasingCurve.Type.InOutQuad: "InOutQuad",
    QEasingCurve.Type.OutInQuad: "OutInQuad",
    QEasingCurve.Type.InCubic: "InCubic",
    QEasingCurve.Type.OutCubic: "OutCubic",
    QEasingCurve.Type.InOutCubic: "InOutCubic",
    QEasingCurve.Type.OutInCubic: "OutInCubic",
    QEasingCurve.Type.InQuart: "InQuart",
    QEasingCurve.Type.OutQuart: "OutQuart",
    QEasingCurve.Type.InOutQuart: "InOutQuart",
    QEasingCurve.Type.OutInQuart: "OutInQuart",
    QEasingCurve.Type.InQuint: "InQuint",
    QEasingCurve.Type.OutQuint: "OutQuint",
    QEasingCurve.Type.InOutQuint: "InOutQuint",
    QEasingCurve.Type.OutInQuint: "OutInQuint",
    QEasingCurve.Type.InSine: "InSine",
    QEasingCurve.Type.OutSine: "OutSine",
    QEasingCurve.Type.InOutSine: "InOutSine",
    QEasingCurve.Type.OutInSine: "OutInSine",
    QEasingCurve.Type.InExpo: "InExpo",
    QEasingCurve.Type.OutExpo: "OutExpo",
    QEasingCurve.Type.InOutExpo: "InOutExpo",
    QEasingCurve.Type.OutInExpo: "OutInExpo",
    QEasingCurve.Type.InCirc: "InCirc",
    QEasingCurve.Type.OutCirc: "OutCirc",
    QEasingCurve.Type.InOutCirc: "InOutCirc",
    QEasingCurve.Type.OutInCirc: "OutInCirc",
    QEasingCurve.Type.InElastic: "InElastic",
    QEasingCurve.Type.OutElastic: "OutElastic",
    QEasingCurve.Type.InOutElastic: "InOutElastic",
    QEasingCurve.Type.OutInElastic: "OutInElastic",
    QEasingCurve.Type.InBack: "InBack",
    QEasingCurve.Type.OutBack: "OutBack",
    QEasingCurve.Type.InOutBack: "InOutBack",
    QEasingCurve.Type.OutInBack: "OutInBack",
    QEasingCurve.Type.InBounce: "InBounce",
    QEasingCurve.Type.OutBounce: "OutBounce",
    QEasingCurve.Type.InOutBounce: "InOutBounce",
    QEasingCurve.Type.OutInBounce: "OutInBounce",
}


mapping = {k: capitalized2snakecase(v) for k, v in mapping.items()}


def ease_template(q_easing_curve):
    name = mapping.get(q_easing_curve)
    def ease_inner(t, parent):
        easing = QEasingCurve(q_easing_curve)
        return easing.valueForProgress(t)

    # Duck typing so everything work when turned into a qgis expression function
    ease_inner.__name__ = name
    ease_inner.__doc__ = """
        <h4>Syntax</h4>
        <p><b>ease_{name}</b>(  <i> t </i>)</p>
        """.format(name=name)
    return ease_inner

for k, v in mapping.items():
    f = ease_template(k)
    # f = qgsfunction(args="auto", group="custom")(f)


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
f = ease_template(QEasingCurve.Type.InCubic)
f(0.2, None)

def bar(a="a", b="b"):
    print(func)
    


def decorater_a(alpha="alpha", beta="beta"):
    def wrapper(func):
        return lambda: print("func name", func.__name__, "arg", alpha)
    return wrapper

def decorater_b(func):
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


@qgsfunction(args="auto", group="custom")
def foo(t, parent):
    return t

def bar(t, parent):
    return t 
bar = qgsfunction(args="auto", group="custom")(bar)
"""


"""
@qgsfunction(args="auto", group="custom")
def foo():
    print("hello")

@qgsfunction(args="auto", group="custom")
def bar(t, parent):
    print("world")
bar = qgsfunction(args="auto", group="custom")(bar)
"""



