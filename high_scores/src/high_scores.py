
import pdb
def latest(scores):
    # scores = [12, 18, 2, 56, 10]
    latest = scores.pop(scores)
    return latest



def personal_best(scores):
    # scores = [12, 18, 2, 56, 10]
    personal_best = scores.max(scores)
    return personal_best


def personal_top_three(scores):
    # scores = [12, 18, 2, 56, 10]
    scores.sort(reverse = True)
    # pdb.set_trace()
    personal_top_three = scores[0:3]

    return personal_top_three

def highest_to_lowest(scores):
    # scores = [12, 18, 2, 56, 10]
    scores.sort(reverse = True)
    # pdb.set_trace()
    # highest_to_lowest = scores
    highest_to_lowest = scores

    return highest_to_lowest