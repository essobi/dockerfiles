FROM python:2.7  
MAINTAINER Graham Gilbert <graham@grahamgilbert.com>  
ENV DOCKER_TRELLO_KEY="null" \  
DOCKER_TRELLO_TOKEN="null" \  
DOCKER_TRELLO_BOARDID="null" \  
DOCKER_TRELLO_TO_DEV_LIST="To Development" \  
DOCKER_TRELLO_DEV_LIST="Development" \  
DOCKER_TRELLO_TO_TEST_LIST="To Testing" \  
DOCKER_TRELLO_TEST_LIST="Testing" \  
DOCKER_TRELLO_TO_PROD_LIST="To Production" \  
DOCKER_TRELLO_MUNKI_PATH="/munki_repo" \  
DOCKER_TRELLO_SUFFIX="Production" \  
DOCKER_DEV_CATALOG="development" \  
DOCKER_TEST_CATALOG="testing" \  
DOCKER_PROD_CATALOG="production" \  
DOCKER_TRELLO_DATE_FORMAT="%d/%m/%y" \  
DOCKER_TRELLO_AUTO_STAGE_TO_TEST="False" \  
DOCKER_TRELLO_AUTO_STAGE_TO_PROD="False" \  
DOCKER_TRELLO_DEV_STAGE_DAYS="0" \  
DOCKER_TRELLO_TEST_STAGE_DAYS="0" \  
DOCKER_TRELLO_PRODUCTION_LIST="null"  
RUN apt-get update && \  
apt-get install -y git && \  
pip install trello && \  
pip install requests[security] && \  
pip install configparser && \  
git clone https://github.com/grahamgilbert/munki-trello.git /munki-trello && \  
git clone https://github.com/munki/munki.git /munki-tools  
COPY write_config.py /write_config.py  
RUN chmod 755 /write_config.py  
COPY run.sh /run.sh  
RUN chmod 755 /run.sh  
CMD /run.sh  

