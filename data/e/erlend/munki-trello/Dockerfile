FROM alpine:3.4  
ENV DOCKER_TRELLO_TO_DEV_LIST="To Development" \  
DOCKER_TRELLO_DEV_LIST="Development" \  
DOCKER_TRELLO_TO_TEST_LIST="To Testing" \  
DOCKER_TRELLO_TEST_LIST="Testing" \  
DOCKER_TRELLO_TO_PROD_LIST="To Production" \  
DOCKER_TRELLO_MUNKI_PATH="/munki_repo" \  
DOCKER_TRELLO_SUFFIX="Production" \  
DOCKER_DEV_CATALOG="development" \  
DOCKER_TEST_CATALOG="testing" \  
DOCKER_PROD_CATALOG="production" \  
DOCKER_TRELLO_TO_DEV_LIST="To Development" \  
DOCKER_TRELLO_TO_TEST_LIST="To Testing" \  
DOCKER_TRELLO_TO_PROD_LIST="To Production" \  
DC_SYNC="true"  
  
RUN apk add --no-cache curl py-pip && \  
pip install trello && \  
curl -L https://github.com/pebbleit/munki-trello/archive/master.tar.gz | tar
zx && \  
curl -L https://github.com/munki/munki/archive/master.tar.gz | tar zx && \  
curl -OL https://github.com/MasteryConnect/docker-
cron/releases/download/v1.3/docker-cron && \  
chmod 0755 docker-cron && \  
apk del curl  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  

