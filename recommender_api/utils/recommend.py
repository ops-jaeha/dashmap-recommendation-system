# Import Library
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Import File
from recommender_api.core.models.lecture import Lecture
from recommender_api.utils import *


def recommend(session: Session, u_id: int = 0):
    if is_watched(session=session, user_id=u_id) is not False:
        lecture, data = recommend_table(session=session)
        user_based_collaborate = cosine_similarity(data, data)
        collaborate_result = pd.DataFrame(data=user_based_collaborate, index=data.index, columns=data.index)

        similar_user = collaborate_result[u_id].sort_values(ascending=False)[:7].index[1]
        lecture_id_lst = data.loc[similar_user].sort_values(ascending=False).index[1:7]
        lecture_url_lst = list(session.query(Lecture).filter(Lecture.id == f"{lecture_id_lst[i]}").one().url
                   for i in range(len(lecture_id_lst)))
        return lecture_id_lst, lecture_url_lst

    else:
        lecture_id_lst = [1, 11, 21, 31, 41, 2]
        lecture_url_lst = list(session.query(Lecture).filter(Lecture.id == f"{lecture_id_lst[i]}").one().url
                               for i in range(len(lecture_id_lst)))
        return lecture_id_lst, lecture_url_lst


def recommend_table(session: Session):
    lecture_data = pd.read_sql_query("SELECT * FROM lecture;", session.bind)
    rating_data = pd.read_sql_query("SELECT * FROM watch_history;", session.bind)
    rating_data.drop('id', axis=1, inplace=True)
    lecture_rating = pd.merge(lecture_data, rating_data, how='right', left_on='id', right_on='lecture_id')
    lecture_rating.drop('id', axis=1, inplace=True)
    lecture_user_rating = lecture_rating.pivot_table('ratings', index='user_id', columns='lecture_id')
    lecture_user_rating.fillna(0, inplace=True)
    return lecture_data, lecture_user_rating