FROM python:2.7  
MAINTAINER Graham Pugh <g.r.pugh@gmail.com>  
ENV DOCKER_STAGING_KEY="null" \  
DOCKER_STAGING_TOKEN="null" \  
DOCKER_STAGING_BOARDID="null" \  
DOCKER_DEV_CATALOG="development" \  
DOCKER_STAGING_TO_DEV_LIST="To Development" \  
DOCKER_STAGING_DEV_LIST="Development" \  
DOCKER_STAGING_DEV_AUTOSTAGE="0" \  
DOCKER_STAGING_DEV_STAGE_DAYS="0" \  
DOCKER_STAGING_DEV_STAGE_TO="Testing" \  
DOCKER_TEST_CATALOG="testing" \  
DOCKER_STAGING_TO_TEST_LIST="To Testing" \  
DOCKER_STAGING_TEST_LIST="Testing" \  
DOCKER_STAGING_TEST_AUTOSTAGE="0" \  
DOCKER_STAGING_TEST_STAGE_DAYS="0" \  
DOCKER_STAGING_TEST_STAGE_TO="Production" \  
DOCKER_PROD_CATALOG="production" \  
DOCKER_STAGING_TO_PROD_LIST="To Production" \  
DOCKER_STAGING_SUFFIX="Production" \  
DOCKER_STAGING_MUNKI_PATH="/munki_repo" \  
DOCKER_STAGING_DEFAULT_REPO="default" \  
DOCKER_STAGING_MAKECATALOGS="/munki-tools/code/client/makecatalogs" \  
DOCKER_STAGING_DATE_FORMAT="%d/%m/%y" \  
DOCKER_STAGING_PRODUCTION_LIST="Production" \  
DOCKER_STAGING_RSSDIR="null" \  
DOCKER_STAGING_RSS_LINK_TEMPLATE="null" \  
DOCKER_STAGING_RSS_GUID_LINK_TEMPLATE="null" \  
DOCKER_STAGING_RSS_CATALOG_LINK_TEMPLATE="null" \  
DOCKER_STAGING_RSS_DESCRIPTION_TEMPLATE="null" \  
DOCKER_STAGING_RSS_ICON_URL_TEMPLATE="null"  
RUN apt-get update -y && \  
apt-get autoremove -y && \  
apt-get install -y git && \  
pip install trello && \  
pip install requests[security] && \  
pip install python-dateutil && \  
pip install configparser && \  
pip install PyRSS2Gen && \  
git clone https://github.com/ox-it/munki-staging.git /etc/munki-staging && \  
git clone https://github.com/munki/munki.git /munki-tools  
COPY munki-staging.cfg /etc/munki-staging/munki-staging-runtime.cfg  
COPY write_config.py /etc/munki-staging/write_config.py  
RUN chmod 755 /etc/munki-staging/write_config.py  
COPY run.sh /etc/munki-staging/run.sh  
RUN chmod 755 /etc/munki-staging/run.sh  
CMD /etc/munki-staging/run.sh  

