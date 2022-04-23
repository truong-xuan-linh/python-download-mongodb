import os
import requests
import matplotlib.pyplot as plt

def download_images(ROOT_dir, urls, user_id):
  start_index = 0
  image_names = []
  i = 0
  try: 
    os.mkdir(os.path.join(ROOT_dir, "images"))
  except:
    pass
  print(f'[GET] Downloading {user_id} ............')
  try:
    os.mkdir(os.path.join(ROOT_dir, "images", user_id))
  except:
    print("User folder already exist")
  while i < len(urls):
    try:
        url_name = urls[i].split("/")[-1]
        url_name = url_name.split(".")[0]
        image_name = user_id + f'_{url_name}.jpg'
        
        result = requests.get(urls[i], timeout=60)

        image_path = os.path.join(ROOT_dir, "images",user_id, image_name)
        with open(image_path, 'wb') as f:
            f.write(result.content)
            f.close()
        try:
            plt.imread(image_path)
            image_names.append(image_name)
            start_index += 1
            i += 1
        except:
            # print('[DELETE] Image has no contents -', image_name)
            os.remove(image_path)
            urls.remove(urls[i])
    except:
        # print('[ERROR] Failed to request -', image_name, '-', urls[i])
        urls.remove(urls[i])