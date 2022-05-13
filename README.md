# MLE-6
This containerized web app implements HuggingFace sentiment analysis using Fast API. It launches a local web server and you can run sentiment analysis by hitting the docs endpoint.

# Step 1. Git Clone this repo locally

Git clone this repo, ensure you have docker installed.

# Step 2 Building the Docker Image

You can then build the Docker image from your files:
```
docker build -t fastapi-demo .
```

# Step 3. Running the Image in a Container

You can then run this image. When you run an image, it's ran in a container. In this case we're connecting port 8000 on our deployment machine (left of the :) with port 8000 (right of the :) in our container.

```
docker run -dp 8000:8000 fastapi-demo
```

# Step 4. Run a query via curl or via FastAPI portal

You can run the curl command below to do a POST request to the docs endpoint and adjust the query string to your liking.

```
curl -X 'POST' \
  'http://localhost:8000/docs' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "query_string": "I love this movie"
}'
```