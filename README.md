# NYC-fire-data-exploration for CIS9760 at Baruch College
Using AWS ec2, opensearch and docker to parse and analyze NYC fire incident dispatch data.

My Big Data class first project where I have to parse data using Docker and ec2 to opensearch and make some visualizations.

That's kinda it

##How to use
After running launching EC2 and opensearch instances, you should paste the folder into your EC2.
Change directory to that folder and build docker image.
```
docker build -t bigdataproject1:1.0 . #bigdataproject1 can be anything you want
```
Then you need to run the image with your parameters
-e INDEX_NAME= index name you'll see in opensearch. Name it whatever you want, I named my "fire"
-e DATASET_ID= id of the dataset you want to use. I used "8m42-w767"
-e APP_TOKEN= your NYC Data API key 
-e ES_HOST= your opensearch endpoint link. I used "https://search-meoooooow-hua5yemsoampwdzur55v25yl64.us-east-2.es.amazonaws.com" 
-e ES_USERNAME= your opensearch master username - "your_username" I wont share mine
-e ES_PASSWORD= your opensearch master password - "your_password" It's a secret
It should look like (I'll leave the dataset_id and es_host as those that I used, others I changed) 
```
docker run -e INDEX_NAME="fire" -e DATASET_ID="8m42-w767" -e APP_TOKEN="your_token_name" -e ES_HOST="https://search-meoooooow-hua5yemsoampwdzur55v25yl64.us-east-2.es.amazonaws.com" -e ES_USERNAME="your_username" -e ES_PASSWORD="your_password" bigdataproject1:1.0 --page_size=6000 --num_pages=1000 #again it can be called whatever you want
```
If you have that you can proceed to finding the dataset you want to explore.
Once you have that you need to get it's dataset identifier.
