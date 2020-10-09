# import standard baseline models
from recommender.algorithms.models import (RecommenderModel,
                                       SVDModel,
                                       ScaledSVD,
                                       CooccurrenceModel,
                                       RandomModel,
                                       PopularityModel)

# import data model
from recommender.algorithms.data import RecommenderData

# import data management routines
from recommender.datasets.movielens import get_movielens_data
from recommender.datasets.bookcrossing import get_bookcrossing_data
from recommender.datasets.netflix import get_netflix_data
from recommender.datasets.amazon import get_amazon_data
