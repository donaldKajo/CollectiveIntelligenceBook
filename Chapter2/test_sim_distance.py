from unittest import TestCase

from Chapter2.SimalarCritics import sim_distance, critics, sim_pearson

critics2 = {"Lisa Rose": {"Lady in the Water": 5.0,
                          "Snakes on a Plane": 5.0,
                          "Just My Luck": 5.0,
                          "Superman Returns": 1.0,
                          "You, Me and Dupree": 1.0,
                          "The Night Listener": 1.0},
            "Gene Seymour": {"Lady in the Water": 1.0,
                             "Snakes on a Plane": 1.0,
                             "Just My Luck": 1.0},
            "Toby": {"Snakes on a Plane": 4.5,
                     "Superman Returns": 4.0,
                     "You, Me and Dupree": 1.0}
            }


class TestSim_distance(TestCase):
    def test_sim_distance(self):
        self.assertAlmostEqual(sim_distance(critics, "Toby", "Jack Matthews"), 0.34, 1)

    def test_sim_distance_same_critic(self):
        self.assertEqual(sim_distance(critics, "Toby", "Toby"), 1)

    def test_pearson_distance(self):
        self.assertAlmostEqual(sim_pearson(critics, "Toby", "Jack Matthews"), 0.66, 1)

    def test_pearson_distance_same_critic(self):
        self.assertEqual(sim_pearson(critics, "Toby", "Toby"), 1)

    def test_pearson_distance_book_example(self):
        self.assertAlmostEqual(sim_pearson(critics, "Lisa Rose", "Gene Seymour"), 0.4, 1)

    # def test_get_recommendation_same_critic(self):
    #     self.assertEqual(getRecommendations(critics2, "Gene Seymour"), 1)
