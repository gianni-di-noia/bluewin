# bluewin

Running this docker compose using `docker-compose up --build` a mongodb instance will be available to the scrapy instance.

At this point visit this [url](http://localhost:9080/crawl.json?spider_name=casinoenlineahex&start_requests=true)

The page will contains the `scrayprt` response in json format.
At the same time a collection `casinos` has been filled in the bluewindow database.

## deploy

`docker-compose up --build`

## todo

- add timestamp to mongo to wrap the casinos base on the request.
- unittests
- 2e2 tests
- documentation
- refactoring and commenting
