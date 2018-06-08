FROM alpine  
MAINTAINER Axel Bock <mr.axel.bock@gmail.com>  
  
EXPOSE 5000  
ADD . /app  
WORKDIR /app  
ENV BUILD_DEPS="python-dev build-base linux-headers py2-pip"  
RUN apk add --no-cache $BUILD_DEPS python \  
&& pip install -r requirements.txt \  
&& apk del $BUILD_DEPS  
  
CMD python flask_app.py  

