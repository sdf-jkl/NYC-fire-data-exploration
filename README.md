# NYC-fire-data-exploration for CIS9760 at Baruch College
Using AWS ec2, opensearch and docker to parse and analyze NYC fire incident dispatch data.

My Big Data class first project where I have to parse data using Docker and ec2 to opensearch and make some visualizations.

That's kinda it

##How to use
After running launching EC2 and opensearch instances, you should paste the folder into your EC2.
Change directory to that folder and build docker image.
```
docker build -t bigdataproject1:1.0 .
```

If you have that you can proceed to finding the dataset you want to explore.
Once you have that you need to get it's dataset identifier.
