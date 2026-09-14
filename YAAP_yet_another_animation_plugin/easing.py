import math

def cubic_bezier(x1,y1,x2,y2):
    #Optimized version of cubic where P_0 = (0,0) and P_3 = (1,1)
    raise NotImplementedError

def clamp01(t: float) -> float:
    return min(max(t, 0.0), 1.0)

def inverse_lerp(a: float, b: float, t: float)->float:
    return clamp01((t - a) / (b - a))

def inverse_lerp_unclamped(a: float, b: float, t: float)->float:
    return (t - a) / (b - a)

def lerp(a: float, b: float, t: float) -> float:
    """
    Linear interpolate on the scale given by a to b, using t as the point on that scale.
    """
    t = clamp01(t)
    return (1.0 - t) * a + t * b

def lerp_unclamped(a: float, b: float, t: float) -> float:
    """Linear interpolate on the scale given by a to b, using t as the point on that scale.
    Examples
    --------
        50 == lerp(0, 100, 0.5)
        4.2 == lerp(1, 5, 0.8)
    """
    return (1 - t) * a + t * b


def linear(start: float, end: float, t: float) -> float:
    """
    Same as lerp
    """
    t = clamp01(t)
    return lerp(start, end, t)

def spring(start: float, end: float, t: float) -> float:
    """
    Hello, World!
    """
    t = clamp01(t)
    t = (math.sin(t * math.pi * (0.2 + 2.5 * t * t * t)) * math.pow(1.0 - t, 2.2) + t) * (1.0 + (1.2 * (1.0 - t)))
    return start + (end - start)  * t

def ease_in_quad(start: float, end: float, t: float) -> float:
    """
    Hello, World!
    """
    t = clamp01(t)
    end -= start
    return end * t * t + start

def ease_out_quad(start: float, end: float, t: float) -> float:
    """
    Hello, World!
    """
    t = clamp01(t)
    return -(end-start) * t * (t - 2) + start

def ease_in_out_quad(start: float, end: float, t: float) -> float:
    """
    Hello, World!
    """
    t = clamp01(t)
    t /= 0.5
    if t < 1.0: return end * 0.5 * t * t + start
    end -= start
    t = t - 1.0
    return -end * 0.5 * (t * (t - 2.0) - 1.0) + start

def ease_in_cubic(start: float, end: float, t: float) -> float:
    """
    Hello, World!
    """
    t = clamp01(t)
    end -= start
    return end * t ** 3 + start

def ease_out_cubic(start: float, end: float, t: float) -> float:
    """
    Hello, World!
    """
    t = clamp01(t)
    t = t - 1.0
    end -= start
    return end * (t ** 3 + 1.0) + start

def ease_in_out_cubic(start: float, end: float, t: float) -> float:
    """
    Hello, World!
    """
    t = clamp01(t)
    t /= 0.5
    end -= start
    if t < 1.0: return end * 0.5 * t ** 3 + start
    t -= 2.0
    return end * 0.5 * (t ** 3 + 2) + start

def ease_in_quart(start: float, end: float, t: float) -> float:
    """
    Hello, World!
    """
    t = clamp01(t)
    end -= start
    return end * t ** 4 + start

def ease_out_quart(start: float, end: float, t: float) -> float:
    """
    Hello, World!
    """
    t = clamp01(t)
    t = t - 1
    end -= start
    return -end * (t ** 4 - 1) + start

def ease_in_out_quart(start: float, end: float, t: float) -> float:
    """
    Hello, World!
    """
    t = clamp01(t)
    t /= 0.5
    end -= start
    if t < 1.0: return end * 0.5 * t ** 4 + start
    t -= 2.0
    return -end * 0.5 * (t ** 4 - 2) + start

def ease_in_quint(start: float, end: float, t: float) -> float:
    """
    Hello, World!
    """
    t = clamp01(t)
    end -= start
    return end * t ** 5 + start

def ease_out_quint(start: float, end: float, t: float) -> float:
    """
    Hello, World!
    """
    t = clamp01(t)
    t = t - 1.0
    end -= start
    return end * (t ** 5 + 1) + start

def ease_in_out_quint(start: float, end: float, t: float) -> float:
    """
    Eases in and out by raising the fraction to the power of 5.
    """
    t = clamp01(t)
    t /= 0.5
    end -= start
    if t < 1.0: return end * 0.5 * t ** 5 + start
    t -= 2.0
    return end * 0.5 * (t ** 5 + 2) + start

def ease_in_sine(start: float, end: float, t: float) -> float:
    """
    Eases in using math.sin.
    """
    t = clamp01(t)
    end -= start
    return -end * math.cos(t * (math.pi * 0.5)) + end + start

def ease_out_sine(start: float, end: float, t: float) -> float:
    """
    Eases in using math.sin.
    """
    t = clamp01(t)
    end -= start
    return end * math.sin(t * (math.pi * 0.5)) + start

def ease_in_out_sine(start: float, end: float, t: float) -> float:
    """
    Eases in using math.sin.
    """
    t = clamp01(t)
    end -= start
    return -end * 0.5 * (math.cos(math.pi * t) - 1.0) + start

def ease_in_expo(start: float, end: float, t: float) -> float:
    """
    Eases in using math.sin.
    """
    t = clamp01(t)
    end -= start
    return end * math.pow(2.0, 10.0 * (t - 1.0)) + start

def ease_out_expo(start: float, end: float, t: float) -> float:
    """
    Eases in using math.sin.
    """
    t = clamp01(t)
    end -= start
    return end * (-math.pow(2.0, -10.0 * t) + 1.0) + start

def ease_in_out_expo(start: float, end: float, t: float) -> float:
    """
    Eases in using math.sin.
    """
    t = clamp01(t)
    t /= 0.5
    end -= start
    if t < 1.0: return end * 0.5 * math.pow(2.0, 10.0 * (t - 1.0)) + start
    t = t - 1
    return end * 0.5 * (-math.pow(2.0, -10.0 * t) + 2.0) + start

def ease_in_circ(start: float, end: float, t: float) -> float:
    """
    Eases in using math.sin.
    """
    t = clamp01(t)
    end -= start
    return -end * (math.sqrt(1.0 - t * t) - 1.0) + start

def ease_out_circ(start: float, end: float, t: float) -> float:
    """
    Eases in using math.sin.
    """
    t = clamp01(t)
    t = t - 1.0
    end -= start
    return end * math.sqrt(1.0 - t * t) + start

def ease_in_out_circ(start: float, end: float, t: float) -> float:
    """
    Eases in using math.sin.
    """
    t = clamp01(t)
    t /= 0.5
    end -= start
    if t < 1.0: return -end * 0.5 * (math.sqrt(1.0 - t * t) - 1.0) + start
    t -= 2.0
    return end * 0.5 * (math.sqrt(1.0 - t * t) + 1) + start

def ease_out_bounce(start: float, end: float, t: float) -> float:
    """
    Eases in using math.sin.
    """
    t = clamp01(t)
    t /= 1.0
    end -= start

    if t < (1.0 / 2.75):
        return end * (7.5625 * t * t) + start
    elif t < (2.0 / 2.75):
        t -= (1.5 / 2.75)
        return end * (7.5625 * t * t + 0.75) + start
    elif t < (2.5 / 2.75):
        t -= (2.25 / 2.75)
        return end * (7.5625 * t * t + 0.9375) + start
    else:
        t -= (2.625 / 2.75)
        return end * (7.5625 * t * t + 0.984375) + start


def ease_in_bounce(start: float, end: float, t: float) -> float:
    """
    Eases in using math.sin.
    """
    t = clamp01(t)
    end -= start
    d = 1.0
    return end - ease_out_bounce(0.0, end, d - t) + start

def ease_in_out_bounce(start: float, end: float, t: float) -> float:
    """
    Eases in using math.sin.
    """
    t = clamp01(t)
    end -= start;
    d = 1.0;
    if t < d * 0.5:
        return ease_in_bounce(0.0, end, t * 2.0) * 0.5 + start
    else:
        return ease_out_bounce(0.0, end, t * 2.0 - d) * 0.5 + end * 0.5 + start