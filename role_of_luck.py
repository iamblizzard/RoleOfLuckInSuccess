#!/usr/bin/python3

import sys
import random
import matplotlib.pyplot as plt

# total no. of people participated in the contest
total_samples = 20000

luck_percentages = [0.001, 0.01, 0.1, 0.2, 0.4, 0.6, 0.8, 1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def get_score(luck_perc):
    random_skill_score = random.randint(1, 100)
    random_luck_score  = random.randint(1, 100)
    luck_factor = (1.0*luck_perc) / 100.0
    score_with_luck    = ((1-luck_factor) * random_skill_score) + (luck_factor * random_luck_score)
    score_without_luck = 1.0*random_skill_score
    return score_with_luck, score_without_luck

def generate_scores(count, luck_perc):
    scores = []
    for i in range(count):
        score_with_luck, score_without_luck = get_score(luck_perc)
        score = {
            'index': i,
            'with_luck': score_with_luck,
            'without_luck': score_without_luck
        }
        scores.append(score)
    return scores

def get_set(scores):
    index_set = set()
    for score in scores:
        index_set.add(score['index'])
    return index_set


if len(sys.argv) != 2:
    exit("Iteration count is missing.....")

iterations = int(sys.argv[1])

# common_percentage = []
avg_common_size = []
for luck_percentage in luck_percentages:
    total_count = 0.0

    for iteration in range(iterations):
        scores = generate_scores(total_samples, luck_percentage)

        top_10_scores_with_luck    = sorted(scores, key=lambda score: score['with_luck'], reverse=True)[:10]
        top_10_scores_without_luck = sorted(scores, key=lambda score: score['without_luck'], reverse=True)[:10]

        without_luck_score_set = get_set(top_10_scores_without_luck)
        with_luck_score_set = get_set(top_10_scores_with_luck)
        
        common_size = len(with_luck_score_set.intersection(without_luck_score_set))
        # total_count += (1.0*common_size / 10.0)
        total_count += common_size

    # common_percentage.append(100*total_count / iterations)
    avg_common_size.append(1.0 * total_count / iterations)

default_x_ticks = range(len(luck_percentages))
plt.xticks(default_x_ticks, luck_percentages)

plt.plot(default_x_ticks, avg_common_size)

plt.xlabel('luck percentage')
# plt.ylabel('percentage of top 10 people with and without luck')
plt.ylabel('avg. persons in top 10 without luck')
# plt.text(0.5, 0.9, "total iterations for each percentage= " + str(iterations),horizontalalignment='right',
#      verticalalignment='top', fontsize=12)

graph_name = "graph-iterations "+str(iterations)+".png"

plt.savefig(graph_name, bbox_inches='tight')
# plt.show()