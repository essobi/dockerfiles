FROM alpine:latest  
MAINTAINER Sergey Kuvakin (lafin)  
  
RUN adduser -D flood && \  
mkdir -p /folder/.session /folder/.db /folder/files /folder/torrents  
  
RUN apk add --update rtorrent supervisor nodejs make g++ openssl python && \  
rm /var/cache/apk/* && \  
wget https://github.com/jfurrow/flood/archive/master.zip && \  
unzip -q master.zip && \  
rm master.zip  
  
COPY config.js /flood-master/config.js  
RUN cd /flood-master && \  
npm install && \  
./node_modules/.bin/gulp dist  
  
COPY supervisord.conf /flood-master/supervisord.conf  
COPY rtorrent.rc /flood-master/.rtorrent.rc  
RUN chown -R flood:flood /flood-master /folder  
  
VOLUME /folder  
EXPOSE 3000  
CMD ["supervisord", "-c", "/flood-master/supervisord.conf"]

