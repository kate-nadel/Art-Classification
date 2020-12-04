import requests
import csv
# import urllib.request
# import pandas as pd

# r = urllib.request.urlopen(url)
# url_ex = "http://www.moma.org/media/W1siZiIsIjU5NDA1Il0sWyJwIiwiY29udmVydCIsIi1yZXNpemUgMzAweDMwMFx1MDAzZSJdXQ.jpg?sha=137b8455b1ec6167"

# mydata_csv_url = 'https://media.githubusercontent.com/media/MuseumofModernArt/collection/master/Artworks.csv'
# df_artworks = pd.read_csv("https://media.githubusercontent.com/media/MuseumofModernArt/collection/master/Artworks.csv", dtype=str)

with open("Artworks.csv","r") as moma_dataset:

    processed_csv = csv.DictReader(moma_dataset)

    # processed_csv["ThumbnailURL"].astype("str")
    #

    # # url = processed_csv[19]


    for row in processed_csv:
        url = row["ThumbnailURL"]
        r = requests.get(url)

        if row["Medium"] == "Gelatin silver print":
            # print(row)
            print(row["ThumbnailURL"])

            with open(("image" + "jpg"), "wb") as f:
# need to create fuction to increase image number so it doesn't rewrite each time?
                f.write(r.content)

            # print(row)




#     for row in processed_csv:
#
#         if row["Medium"] !== "Gelatin silver print":
#
#

#
#     f.write(r.content)
