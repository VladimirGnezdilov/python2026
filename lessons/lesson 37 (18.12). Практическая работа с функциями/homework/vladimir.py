def rectangle_info(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter


def is_adult(age):
    return age >= 18


def safe_div(a, b):
    if b == 0:
        return None
    return a / b


def delivery_price(city, weight_kg, urgent):
    if urgent:
        return 500 + 30 * weight_kg
    else:
        return 300 + 20 * weight_kg
price1 = delivery_price("Городок", 2, False)
price2 = delivery_price("Городище", 5, True)

def push_score(score, scores=None):
    if scores is None:
        scores = []
    scores.append(score)
    return scores
  
result1 = push_score(85)
result2 = push_score(90)

def top_scores(scores, n=3):
    sorted_scores = sorted(scores, reverse=True)
    return sorted_scores[:n]

def make_multiplier(factor):
    def mul(x):
        return x * factor
    return mul



def mean(*args):
    if not args:
        return None
    return sum(args) / len(args)
