FROM python:3.5.2-alpine  
  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV PYTHONIOENCODING UTF-8  
  
COPY requirements.txt /tmp/  
  
RUN mkdir -p /usr/src/app \  
&& echo "@edgecommunity http://dl-cdn.alpinelinux.org/alpine/edge/community"
>> /etc/apk/repositories \  
&& apk --no-cache add \  
ca-certificates \  
freetype \  
libpng \  
&& apk --no-cache -f add \  
openblas@edgecommunity \  
openblas-ilp64@edgecommunity \  
&& apk --no-cache add --virtual build-dependencies \  
build-base \  
freetype-dev \  
gfortran \  
libpng-dev \  
&& apk --no-cache add \  
openblas-dev@edgecommunity \  
&& ln -s /usr/include/locale.h /usr/include/xlocale.h \  
&& pip install --no-cache-dir -U \  
pip \  
setuptools \  
wheel \  
&& cd /tmp \  
&& echo "Installing python packages ..." \  
&& pip install --no-cache-dir -r requirements.txt \  
&& echo "Removing OpenBLAS buildtime dependencies ... " \  
&& apk del -f openblas-dev \  
&& echo "Removing buildtime dependencies ... " \  
&& apk del -f build-dependencies \  
&& cd /usr/src/app/  
  
WORKDIR /usr/src/app  

