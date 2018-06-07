ARG GEONODE_DJANGO_BASE_TAG=latest  
FROM kartoza/geonode_django_base:${GEONODE_DJANGO_BASE_TAG}  
  
# Toolbox  
RUN apt-get -y update; apt-get -y install git python-pip python-virtualenv  
# include uwsgi and production ready  
RUN apt-get update -y; apt-get -y --force-yes install \  
python-gdal \  
python-geoip \  
npm \  
nodejs \  
rpl  
RUN npm -g install yuglify  
RUN rpl "env node" "env nodejs"
/usr/local/lib/node_modules/yuglify/bin/yuglify  
ADD uwsgi.conf /uwsgi.conf  
  
# Clone source code  
WORKDIR /tmp  
ARG DOCKER_GEOSAFE_TAG=develop  
RUN git clone \--branch ${DOCKER_GEOSAFE_TAG} \--depth 1
https://github.com/kartoza/docker-geosafe.git  
RUN mv /tmp/docker-geosafe/src/core /usr/src/core  
  
WORKDIR /usr/src/app  
  
# Upgrade dependencies  
RUN apt-get update -y; apt-get install -y gdal-bin  
ADD uninstall.txt /uninstall.txt  
RUN pip uninstall -y -r /uninstall.txt  
ADD REQUIREMENTS.txt /REQUIREMENTS.txt  
RUN pip install --upgrade -r /REQUIREMENTS.txt  
ADD entry-point.sh /entry-point.sh  
RUN chmod +x /entry-point.sh  
  
CMD ["uwsgi", "--ini", "/uwsgi.conf"]  

