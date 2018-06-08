FROM anapsix/alpine-java:8_jdk  
  
MAINTAINER Guillaume Lefevre <gelefevre@octo.com>  
  
RUN mkdir /floodlight  
WORKDIR /floodlight  
  
RUN apk add --no-cache gcc g++ make libc-dev apache-ant python-dev git && \  
apk add maven --update-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/community/ && \  
git clone git://github.com/floodlight/floodlight.git /floodlight && \  
git submodule init && \  
git submodule update && \  
ant && \  
mkdir /var/lib/floodlight && \  
chmod 777 /var/lib/floodlight && \  
apk del git apache-ant gcc make python-dev libc-dev g++ maven && \  
rm -rf /var/cache/apk/*  
  
EXPOSE 8080 6653  
  
CMD java -jar target/floodlight.jar  

