terraform init

cp -r Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/spotipy ../lambda_payloads/spotify_analyzer_payload/
cp -r /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/dotenv/ ../lambda_payloads/spotify_analyzer_payload/

cp /Users/jordan/dev/projects/spotify-api-pipeline/config/playlist_uri_lib.py ../lambda_payloads/spotify_analyzer_payload/
cp /Users/jordan/dev/projects/spotify-api-pipeline/playlist.py ../lambda_payloads/spotify_analyzer_payload/
cp /Users/jordan/dev/projects/spotify-api-pipeline/spotify_analyzer.py ../lambda_payloads/spotify_analyzer_payload/

zip -r ../payload.zip *

cd ../.tf/

terraform plan
