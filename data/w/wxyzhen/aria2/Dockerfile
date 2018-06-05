FROM alpine:edge  
MAINTAINER wxyzhen  
  
ENV ARIA2_VERSION 1.31.1  
ENV GOSU_VERSION 1.10  
  
RUN set -xe \  
&& apk update \  
&& apk add aria2 --no-cache \  
&& aria2c https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-
amd64 -o /usr/local/bin/gosu \  
&& chmod a+x usr/local/bin/gosu \  
&& adduser -D aria2 \  
&& mkdir -p /home/aria2/downloads \  
&& touch /home/aria2/downloads/aria2.session  
  
COPY aria2.conf /home/aria2/aria2.conf  
  
RUN chown aria2 /home/aria2 -R  
  
VOLUME /home/aria2/downloads  
  
EXPOSE 6800  
  
CMD set -xe \  
&& gosu aria2 aria2c --conf-path=/home/aria2/aria2.conf  

