FROM alpine:latest  
  
RUN \  
apk update && \  
apk add git python py-pip build-base python-dev py-pip jpeg-dev zlib-dev
mariadb-dev && \  
cp /lib/libz.so /usr/lib/ && \  
cp /lib/libz.a /usr/lib/ && \  
pip install awsebcli && \  
pip install awscli  

