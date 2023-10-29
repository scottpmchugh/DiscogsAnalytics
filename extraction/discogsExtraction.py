import discogs_client
import config

#Connect using auth token
d = discogs_client.Client('discogsAnalytics', user_token=config.discogs_token)
me=d.identity()

for album in me.collection_folders[1].releases:
   print([album.release.title],[album.release.artists_sort],[album.release.genres])

  