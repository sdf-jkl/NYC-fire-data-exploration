# NYC-fire-data-exploration for CIS9760 at Baruch College
Using AWS ec2, opensearch and docker to parse and analyze NYC fire incident dispatch data.

My Big Data class first project where I have to parse data using Docker and ec2 to opensearch and make some visualizations.

That's kinda it

## How to use
After running launching EC2 and opensearch instances, you should paste the folder into your EC2.
Change directory to that folder and build docker image.

You should know which variables you want to use and create mapping for them in main.py file
```
docker build -t bigdataproject1:1.0 . #bigdataproject1 can be anything you want
```
Then you need to run the image with your parameters in session manager.

-e INDEX_NAME= index name you'll see in opensearch. Name it whatever you want, I named my "fire"

-e DATASET_ID= id of the dataset you want to use. I used "8m42-w767"

-e APP_TOKEN= your NYC Data API key - "your_token_name"

-e ES_HOST= your opensearch endpoint link. I used "https://search-meoooooow-hua5yemsoampwdzur55v25yl64.us-east-2.es.amazonaws.com" 

-e ES_USERNAME= your opensearch master username - "your_username" I wont share mine

-e ES_PASSWORD= your opensearch master password - "your_password" It's a secret

--page_size= amount of rows you want to extract(don't make it too big, cause it crashed my EC2 instance when I used 60k last time, to run it final time for my project I used 6000.)

--numm_pages= optional parameter for extracting more data than page_size can handle at once. I used 1000, making it total 6mil rows.


It should look like this:
```
docker run -e INDEX_NAME="fire" -e DATASET_ID="8m42-w767" -e APP_TOKEN="your_token_name" -e ES_HOST="https://search-meoooooow-hua5yemsoampwdzur55v25yl64.us-east-2.es.amazonaws.com" -e ES_USERNAME="your_username" -e ES_PASSWORD="your_password" bigdataproject1:1.0 --page_size=6000 --num_pages=1000 #again it can be called whatever you want
```

## Questions that I want to answer by exploring this dataset

1. Compare average response time in boroughs. (I wanted to do it with all zipcodes compared to mine, but I forgot to include zipcode as a variable while uploading the data.)
2. Compare amount of engines assigned to different incident type. (What incident type has biggest amount of engines assigned?)
3. See which incidents in each borough make up total amount of incidents. (I really want to use heatmap for something.)
4. Compare average amount of engines per day in boroughs. (I can't come up with interesting questions)
