import discogs_client
import config
import pandas as pd

#Connect using auth token
d = discogs_client.Client('discogsAnalytics', user_token=config.discogs_token)
me=d.identity()

collection_data = []
for album in me.collection_folders[1].releases:
   data = [album.release.artists[0].name,
   album.release.title,
   album.release.genres[0]]
   collection_data.append(data)
df = pd.DataFrame(collection_data, columns=['Artists','Title','Genre'])
print(df)