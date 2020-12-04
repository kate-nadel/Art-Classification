import requests
import os



url = "http://www.moma.org/media/W1siZiIsIjk3Il0sWyJwIiwiY29udmVydCIsIi1yZXNpemUgMzAweDMwMFx1MDAzZSJdXQ.jpg?sha=55b65fa4368fe00a"

r = requests.get(url)

# with open(("image" + "jpg"), "wb") as f:
with open(("newimage" + {currentCount+1} + ".jpg"), "wb") as f:

    f.write(r.content)
