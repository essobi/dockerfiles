FROM alpine:latest  
MAINTAINER Peter Winter <peter@pwntr.com>  
  
# create dirs for the config, the music, and the music to be imported  
RUN mkdir /config /music /import  
  
# set the beets dir environment variable. This tells beets where to store
configs, dbs, plugin sidecar files etc.  
ENV BEETSDIR /config  
  
# copy the config from the project folder into the container  
COPY config.yaml /config/config.yaml  
  
# update the base system  
RUN apk update && apk upgrade  
  
# install python 2, GNU wget (replacing busybox' wget), imagemagick, and clear
the cache afterwards  
RUN apk add python py-pip wget imagemagick && rm -rf /var/cache/apk/*  
  
# upgrade pip and install beets with some useful plugins and requirements  
RUN pip install -U pip && \  
pip install beets requests discogs-client pylast
https://github.com/ocelma/python-itunes/archive/master.zip  
  
VOLUME /config /music /import  
  
ENTRYPOINT ["beet"]  
  
# by default, import everything from within the /import dir when starting this
container  
CMD ["import", "/import"]  

