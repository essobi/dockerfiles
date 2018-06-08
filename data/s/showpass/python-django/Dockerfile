FROM python:2.7-alpine3.4  
ENV PYTHONUNBUFFERED 1  
# Install Python dependencies  
RUN echo "http://dl-2.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories; \  
echo "http://dl-3.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories; \  
echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories;  
RUN apk -q update  
RUN apk -q --no-cache add py-psycopg2 postgresql-dev # PostgreSQL  
RUN apk -q --no-cache add py-gdal geos-dev geoip-dev gdal-dev # PostGIS  
RUN apk -q --no-cache add linux-headers # psutil  
RUN apk -q --no-cache add bash # bash  
RUN apk -q --no-cache add libevent-dev # Gevent  
RUN apk -q add --update curl curl-dev openssl # Curl  
RUN apk -q --no-cache add py-pip gcc musl-dev libjpeg-turbo-dev python-dev
zlib-dev libffi-dev build-base jpeg-dev freetype-dev # Pillow  
RUN apk -q --no-cache add git # Git  
RUN apk -q --no-cache add nano htop postgresql-client # Debugging  
RUN apk -q --no-cache add libxslt-dev libxml2-dev # lxml  
  
ENV LIBRARY_PATH /lib:/usr/lib:$LIBRARY_PATH # Pillow  
ADD requirements.txt .  
RUN pip install -r requirements.txt # Install dependencies that take a long
time  
RUN rm requirements.txt  

