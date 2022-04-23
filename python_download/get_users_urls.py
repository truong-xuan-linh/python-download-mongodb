import pandas as pd

def get_users_urls(df_dir = "/content/users.xlsx"):
  df = pd.read_excel(df_dir)
  users_dict = dict()
  for i in df.index:
    if df['user_id'][i] not in users_dict:
      users_dict[df['user_id'][i]] = [df['url'][i]]
    else:
      users_dict[df['user_id'][i]].append(df['url'][i])
  users_dict = dict(sorted(users_dict.items()))
  return users_dict

# from bson.regex import Regex
# from pymongo import MongoClient
# def get_users_urls():
#     client = MongoClient("mongodb://root:%601234qwer%60@10.10.12.201:27017,10.10.12.202:27017,10.10.12.203:27017/?replicaSet=test&authSource=admin")
#     database = client["test-api-halo"]
#     collection = database["m200"]

#     pipeline = [{
#         "$match": {
#             "mv206": Regex("^(?:http(s)?:\\/\\/)?[\\w.-]+(?:\\.[\\w\\.-]+)+[\\w\\-\\._~:/?#[\\]@!\\$&'\\(\\)\\*\\+,;=.]+$", "gm")
#         }
#     }, {
#         "$sort": {
#             "pn100": 1
#         }
#     }, {
#         "$project": {
#             "user_id": "$pn100",
#             "url": "$mv206"
#         }
#     }, {
#         "$match": {
#             "user_id": {
#                 "$ne": None
#             }
#         }
#     }]

#     # Created with NoSQLBooster, the essential IDE for MongoDB - https://nosqlbooster.com
#     cursor = collection.aggregate(pipeline)
#     users_dict = dict()
#     for doc in cursor:
#       if doc['user_id'] not in users_dict:
#         users_dict[doc['user_id']] = [doc['url']]
#       else:
#         users_dict[doc['user_id']].append(doc['url'])
#     users_dict = dict(sorted(users_dict.items()))
#     return users_dict
#     # try:
#     #     for doc in cursor:
#     #         print(doc["url"])
#     #         break
#     # finally:
#     #     cursor.close()
