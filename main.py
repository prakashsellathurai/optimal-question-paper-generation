import input

from collections import namedtuple

Item = namedtuple('Item', 'name value weight')

def knapsack(allowed_weight, items):
    """
    Given a list of items with name, value and weight.
    Return the optimal value with total weight <= allowed weight and 
    list of picked items.
    """ 
    k = [
        [0 for x in range(allowed_weight + 1)]
        for x in range(len(items) + 1)
    ]

    for next_idx, (item, weights) in enumerate(zip(items, k), 1):
        for w, current_weight in enumerate(weights[1:], 1):
            if item.weight <= w:
                k[next_idx][w] = max(
                    item.value + weights[w - item.weight],
                    current_weight
                )
            else:
                k[next_idx][w] = current_weight

    return k[-1][-1], list(fetch_items(k, allowed_weight, items))

# find which item are picked
def fetch_items(k, allowed_weight, items):
    for item, weights_p, weights_n in zip(items[::-1], k[-2::-1], k[::-1]):
        if weights_n[allowed_weight] != weights_p[allowed_weight]:
            yield item
            allowed_weight -= item.weight

def question_generator(json):
    required_easy_questions_marks = int(json["total_marks"]) * int(json["easy_percentage"]) / 100
    required_medium_questions_marks = int(json["total_marks"]) * int(json["medium_percentage"]) / 100
    required_hard_questions_marks = int(json["total_marks"]) * int(json["hard_percentage"]) / 100
    
    sum = required_easy_questions_marks + required_medium_questions_marks + required_hard_questions_marks
    
    if (sum != int(json["total_marks"])):
        print("check your mark splitting percentage it is not consistent ")
    else:
        items = []
        for item in json["questions"]:
            if item["difficulty"] == "easy":
                difficulty = 1
            elif item["difficulty"] == "medium":
                difficulty = 2
            else: 
                 difficulty = 3
            items.append(Item(item["id"],difficulty,int(item["marks"])))
            
        return knapsack(int(json["total_marks"]), items)

if __name__ == '__main__':
    json = input.input_parser("input.txt")
    max_value, picked = question_generator(json)
    for item in reversed(picked):
        print(item.name)