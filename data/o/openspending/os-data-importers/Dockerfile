FROM python:3.6-alpine  
  
RUN apk add --update --no-cache \  
build-base \  
ca-certificates \  
g++ \  
redis \  
git \  
libffi \  
libffi-dev \  
libpq \  
libxml2-dev \  
libxslt-dev \  
nodejs \  
python3-dev \  
wget \  
libstdc++ \  
postgresql-dev  
RUN apk --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --update
add leveldb leveldb-dev  
RUN update-ca-certificates  
RUN mkdir -p /var/redis && chmod 775 /var/redis && chown redis.redis
/var/redis  
  
WORKDIR /app  
  
# Add requirements files before to avoid rebuilding dependencies  
# every time any file is modified.  
ADD package.json .  
ADD npm-shrinkwrap.json .  
RUN npm install  
  
ADD eu-structural-funds/requirements.txt eu-structural-funds/requirements.txt  
RUN pip3 install -r eu-structural-funds/requirements.txt  
  
ADD requirements.txt .  
RUN pip3 install -r requirements.txt  
  
ADD . .  
  
ENV PATH "$PATH:/app/node_modules/.bin"  
ENV DPP_REDIS_HOST 127.0.0.1  
ENV DPP_CELERY_BROKER redis://localhost:6379/6  
ENV GIT_REPO=https://github.com/openspending/os-data-importers.git  
  
EXPOSE 5000  
CMD /app/initialize.sh  
  

