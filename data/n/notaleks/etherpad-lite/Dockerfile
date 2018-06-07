# Stable version of etherpad doesn't support npm 2  
FROM ubuntu:xenial  
MAINTAINER sign2  
  
ENV ETHERPAD_VERSION 1.6.0  
RUN apt-get update && \  
apt-get install -y curl unzip nodejs-legacy npm mysql-client abiword && \  
rm -r /var/lib/apt/lists/*  
  
ADD . /var/www/etherpad  
  
WORKDIR /var/www/etherpad  
  
EXPOSE 9001  
CMD ["bin/run.sh", "--root"]  

