FROM tomcat:jre8-alpine  
MAINTAINER William Weiskopf <william@weiskopf.me>  
  
ENV LIBRESONIC_VERSION 6.1  
# Install libresonic and its dependencies  
RUN apk add --no-cache \  
# Install dependencies  
ca-certificates \  
ffmpeg \  
flac \  
lame \  
# Download the official libresonic package  
&& apk add \--no-cache --virtual=build-dependencies \  
wget \  
&& rm -rf /usr/local/tomcat/webapps/* \  
&& wget https://libresonic.org/release/libresonic-v$LIBRESONIC_VERSION.war -O
/usr/local/tomcat/webapps/ROOT.war \  
&& apk del build-dependencies  
  
# Create the main folder  
RUN mkdir /var/libresonic  
  
# Create data directories and symlinks to make it easier to use a volume  
RUN mkdir /data \  
&& cd /data \  
&& mkdir db jetty lucene2 lastfmcache thumbs music Podcast playlists \  
&& touch libresonic.properties libresonic.log \  
&& ln -s /data/* /var/libresonic  
  
# create transcode folder and add binaries  
RUN mkdir /var/libresonic/transcode \  
&& cd /var/libresonic/transcode \  
&& ln -s /usr/bin/ffmpeg \  
&& ln -s /usr/bin/flac \  
&& ln -s /usr/bin/lame  
  
# Use the libresonic user for everything  
RUN adduser -h /var/libresonic -D libresonic \  
&& chown -R libresonic:libresonic /data \  
&& chown -R libresonic:libresonic /usr/local/tomcat \  
&& chown -R libresonic:libresonic /var/libresonic  
  
EXPOSE 8080  
USER libresonic  
VOLUME ["/data"]  
WORKDIR /var/libresonic  
  

