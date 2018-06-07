FROM python:2.7.13-alpine3.6  
  
RUN set -x \  
&& apk --update --no-cache add make \  
&& apk --update --no-cache --virtual .build-dep add \  
build-base \  
linux-headers \  
&& pip install --upgrade pip \  
&& pip install --no-cache-dir falcon \  
&& pip install --no-cache-dir ujson \  
&& pip install --no-cache-dir cython \  
&& pip install --no-cache-dir --no-binary :all: falcon \  
&& pip install --no-cache-dir
https://github.com/unbit/uwsgi/archive/uwsgi-2.0.zip#egg=uwsgi \  
&& apk del .build-dep  

