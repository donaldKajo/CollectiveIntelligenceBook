from math import sqrt

critics = {"Lisa Rose": {"Lady in the Water": 2.5,
                         "Snakes on a Plane": 3.5,
                         "Just My Luck": 3.0,
                         "Superman Returns": 3.5,
                         "You, Me and Dupree": 2.5,
                         "The Night Listener": 3.0},
           "Gene Seymour": {"Lady in the Water": 3.0,
                            "Snakes on a Plane": 3.5,
                            "Just My Luck": 1.5,
                            "Superman Returns": 5.0,
                            "You, Me and Dupree": 3.5,
                            "The Night Listener": 3.0},
           "Michael Phillips": {"Lady in the Water": 2.5,
                                "Snakes on a Plane": 3.0,
                                "Superman Returns": 3.5,
                                "The Night Listener": 4.0},
           "Claudia Puig": {"Snakes on a Plane": 3.5,
                            "Just My Luck": 3.0,
                            "Superman Returns": 4.0,
                            "You, Me and Dupree": 2.5,
                            "The Night Listener": 4.5},
           "Mick LaSalle": {"Lady in the Water": 3.0,
                            "Snakes on a Plane": 4.0,
                            "Just My Luck": 2.0,
                            "Superman Returns": 3.0,
                            "You, Me and Dupree": 2.0,
                            "The Night Listener": 3.0},
           "Jack Matthews": {"Lady in the Water": 3.0,
                             "Snakes on a Plane": 4.0,
                             "Superman Returns": 5.0,
                             "You, Me and Dupree": 3.5,
                             "The Night Listener": 3.0},
           "Toby": {"Snakes on a Plane": 4.5,
                    "Superman Returns": 4.0,
                    "You, Me and Dupree": 1.0}
           }


# One distance metric is the Euclidean metric
def sim_distance(prefs, person1, person2):
    si = find_common_watched_movies(prefs, person1, person2)

    # if no ratings in common, return 0
    if len(si) == 0:
        return 0

    sum_of_squares = sum(pow(prefs[person1][item] - prefs[person2][item], 2) for item in si.keys())

    return sqrt(1 / (1 + sum_of_squares))


def sim_pearson(prefs, person1, person2):
    similar_interests = find_common_watched_movies(prefs, person1, person2)

    n = len(similar_interests)
    if n == 0:
        return -0

    # Add up all the preferences for each critic
    sump1 = sum([prefs[person1][item] for item in similar_interests])
    sump2 = sum([prefs[person2][item] for item in similar_interests])

    # Add sum of squares for each person
    sump1square = sum([pow(prefs[person1][item], 2) for item in similar_interests])
    sump2square = sum([pow(prefs[person2][item], 2) for item in similar_interests])

    # Find the cross product
    pSum = sum([prefs[person1][item] * prefs[person2][item] for item in similar_interests])

    # calculate and return the final Pearson coefficient which should be between -1 and 1
    numerator = pSum - (sump1 * sump2) / n
    denominator = sqrt((sump1square - pow(sump1, 2) / n) * (sump2square - pow(sump2, 2) / n))

    if denominator == 0:
        return 0

    return numerator / denominator


def find_common_watched_movies(prefs, person1, person2):
    # initialize common preferences dictionary
    si = {}

    # find movies in common
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    return si


def getRecommendations(prefs, person, similarity=sim_pearson):
    totals = {}
    simSum = {}
    for other in prefs:
        if other != person:
            sim = similarity(prefs, person, other)
            if sim > 0:
                for item in prefs[other]:
                    if item not in prefs[person] or prefs[person][item] == 0:
                        # Similarity * score for movie
                        totals.setdefault(item, 0)
                        totals[item] += prefs[other][item] * sim
                        simSum.setdefault(item, 0)
                        simSum[item] += sim

    rankings = [(total/simSum[item], item) for item, total in totals.items()]

    rankings.sort()
    rankings.reverse()
    return rankings


if __name__ == "__main__":
    print(sim_distance(critics, "Toby", "Jack Matthews"))
    print(sim_pearson(critics, "Toby", "Jack Matthews"))
    print(getRecommendations(critics, "Michael Phillips"))
