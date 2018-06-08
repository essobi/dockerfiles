FROM python:3-alpine  
  
RUN set -x \  
&& apk \--update \--no-cache add make \  
&& apk \--update \--no-cache \--virtual .build-dep add \  
build-base \  
&& pip install \--upgrade pip \  
&& pip install cython \  
&& apk del .build-dep

