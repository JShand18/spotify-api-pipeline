# terraform init 

# terraform import aws_security_group.sg_redshift sg-0db81cd61e638a6d8
# terraform import aws_redshift_cluster.redshift redshift-cluster-pipeline
# terraform import aws_iam_policy.lambda_execution_policy arn:aws:iam::328289421223:policy/lambda_execution_policy

rm ../payload.zip

cp -r /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/spotipy ../lambda_payloads/spotify_analyzer_payload/
cp -r /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/dotenv ../lambda_payloads/spotify_analyzer_payload/
cp -r /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/redis ../lambda_payloads/spotify_analyzer_payload/
cp -r /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/requests ../lambda_payloads/spotify_analyzer_payload/


cp /Users/jordan/dev/projects/spotify-api-pipeline/config/playlist_uri_lib.py ../lambda_payloads/spotify_analyzer_payload/config/
cp /Users/jordan/dev/projects/spotify-api-pipeline/playlist.py ../lambda_payloads/spotify_analyzer_payload/
cp /Users/jordan/dev/projects/spotify-api-pipeline/spotify_analyzer.py ../lambda_payloads/spotify_analyzer_payload/

cd ../lambda_payloads/spotify_analyzer_payload/

zip -r ../../payload.zip *

cd ../../.tf/

terraform fmt
terraform validate

terraform plan 
