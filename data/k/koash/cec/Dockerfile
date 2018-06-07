FROM alpine:3.6  
  
MAINTAINER koash  
  
RUN apk --no-cache add \  
python \  
python-dev \  
py-setuptools \  
&& apk add --no-cache --virtual build-dependencies \  
g++ \  
py-pip \  
&& ln -s /usr/include/locale.h /usr/include/xlocale.h \  
&& pip install --upgrade pip \  
&& pip install numpy \  
&& pip install pandas \  
&& pip install chardet \  
&& apk del --purge build-dependencies  

