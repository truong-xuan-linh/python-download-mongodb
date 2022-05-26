import os
from get_users_urls import get_users_urls
from download_images import download_images

def main(ROOT_dir):
  users_dict = get_users_urls()
  for user_id in users_dict: 
    len_url = len(os.path.join(ROOT_dir, "images"))
    while len_url > 2:
      continue
    download_images(ROOT_dir, users_dict[user_id], user_id)
  os.mkdir(os.path.join(ROOT_dir, "images", "zzzz"))

if __name__ == '__main__':
  ROOT_dir = os.getenv('DEEPFACE_DATA')
  main(ROOT_dir)

