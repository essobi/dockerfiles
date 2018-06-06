FROM buildpack-deps:latest  
MAINTAINER Daan Sprenkels "hello@dsprenkels.com"  
  
ENV CLEAN_ARCHIVE=clean2.4_64.tar.gz  
ENV
CLEAN_DOWNLOAD_URL=http://clean.cs.ru.nl/download/Clean24/linux/$CLEAN_ARCHIVE  
  
RUN curl -fsOSL $CLEAN_DOWNLOAD_URL \  
&& mkdir -p /tmp/clean \  
&& tar -C /tmp/clean -xzf $CLEAN_ARCHIVE \--strip-components=1 \  
&& make -C /tmp/clean -e INSTALL_DIR=/usr/local/ \  
&& rm -rf $CLEAN_ARCHIVE /tmp/clean/ \  

