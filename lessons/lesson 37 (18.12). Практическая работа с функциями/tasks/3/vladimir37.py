scores=[]
def push_score(score, scores=None):
    if scores is None:
        scores = []
    scores.append(score)
    return scores
print(push_score("1231"))
print(push_score("1232"))
print(push_score("1231",scores))


def top_scores(scores, n=3):
   return sorted(scores, reverse=True)[:n]
