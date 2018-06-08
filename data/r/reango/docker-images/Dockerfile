FROM node:8.9.2-alpine  
  
ENV INSTALL_PATH=/reango/ \  
REPO_URL=https://github.com/ncrmro/reango/archive/master.tar.gz  
# BUILD_PACKAGES="apt-transport-https python-software-properties"  
  
WORKDIR $INSTALL_PATH  
  
# Docker hub only downloads the tar where as building locally auto untars it  
#ADD https://github.com/ncrmro/reango/archive/master.tar.gz $INSTAL_PATH  
RUN apk update && apk add ca-certificates wget  
# Set up DIR  
RUN wget $REPO_URL && tar xvzf master.tar.gz && rm master.tar.gz && \  
mv $INSTALL_PATH\reango-master/* $INSTALL_PATH && rm -r $INSTALL_PATH\reango-
master  
# Notes on making image smaller  
# Celery beat or Scrappy libxml2 libxml2-dev  
# Psycopg2 python3 python3-dev postgresql-dev  
# Gitlab checkout Git  
  
RUN apk add -U --no-cache python3 ca-certificates postgresql-dev gcc
python3-dev musl-dev git libffi libffi-dev linux-headers libxml2 libxml2-dev
libxslt-dev && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --no-cache-dir --upgrade pip setuptools && \  
rm -r /root/.cache && \  
pip3 install --no-cache-dir -r $INSTALL_PATH\lib/deps/prod.txt && \  
npm cache clean --force && \  
yarn --ignore-scripts && yarn cache clean && \  
apk del musl-dev zlib-dev openssl-dev  
  
# docker build -t ncrmro/adbase:alpine . && docker push ncrmro/adbase:alpine  
# Original is 365MB at time of creation

