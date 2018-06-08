FROM debian:wheezy  
MAINTAINER Graham Gilbert <graham@pebbleit.com>  
ENV DOCKER_TRELLO_TO_DEV_LIST="To Development" \  
DOCKER_TRELLO_DEV_LIST="Development" \  
DOCKER_TRELLO_TO_TEST_LIST="To Testing" \  
DOCKER_TRELLO_TEST_LIST="Testing" \  
DOCKER_TRELLO_TO_PROD_LIST="To Production" \  
DOCKER_TRELLO_MUNKI_PATH="/munki_repo" \  
DOCKER_TRELLO_SUFFIX="Production" \  
DOCKER_DEV_CATALOG="development" \  
DOCKER_TEST_CATALOG="testing" \  
DOCKER_PROD_CATALOG="production"  
RUN apt-get update && \  
apt-get install -y git && \  
apt-get install -y python-pip && \  
pip install trello && \  
git clone https://github.com/pebbleit/munki-trello.git /munki-trello && \  
git clone https://github.com/munki/munki.git /munki-tools  
CMD python /munki-trello/munki-trello.py --key $DOCKER_TRELLO_KEY \--token
$DOCKER_TRELLO_TOKEN \--boardid $DOCKER_TRELLO_BOARDID \--to-dev-list
"$DOCKER_TRELLO_TO_DEV_LIST" \--dev-list "$DOCKER_TRELLO_DEV_LIST" \--to-test-
list "$DOCKER_TRELLO_TO_TEST_LIST" \--test-list "$DOCKER_TRELLO_TEST_LIST"
\--to-prod-list "$DOCKER_TRELLO_TO_PROD_LIST" \--dev-catalog
"$DOCKER_DEV_CATALOG" \--test-catalog "$DOCKER_TEST_CATALOG" \--prod-catalog
"$DOCKER_PROD_CATALOG" \--repo-path "$DOCKER_TRELLO_MUNKI_PATH" \--suffix
"$DOCKER_TRELLO_SUFFIX" \--makecatalogs /munki-tools/code/client/makecatalogs  

