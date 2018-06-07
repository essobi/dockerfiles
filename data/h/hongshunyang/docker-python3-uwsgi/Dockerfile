FROM hongshunyang/docker-python3  
MAINTAINER Hongshun Yang <yanghongshun@outlook.com>  
  
RUN apk add -U --virtual build-deps python3-dev build-base zlib-dev jpeg-dev \  
libffi-dev openssl-dev libxslt-dev libxml2-dev freetype-dev linux-headers \  
&& ln -s /usr/include/locale.h /usr/include/xlocale.h \  
&& pip install virtualenv uwsgi \  
&& apk del -U --purge build-deps \  
&& apk add -U libxml2  
  

