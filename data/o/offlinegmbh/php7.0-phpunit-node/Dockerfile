FROM offlinegmbh/php7.0-phpunit  
MAINTAINER Tobias Kuendig <tobias@offline.swiss>  
  
RUN apt-get update && apt-get -y install nodejs nodejs-legacy npm && apt-get
-y autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*  
  
EXPOSE 8008  
  
WORKDIR /tmp/code  
  

