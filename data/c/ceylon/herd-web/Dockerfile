#  
# Image for running the Ceylon Herd server  
#  
FROM ceylon/base-debian:java7  
  
MAINTAINER Tako Schotanus <tako@ceylon-lang.org>  
  
LABEL org.ceylon-lang.dockerfile.description="Image for running the Ceylon
Herd server" \  
org.ceylon-lang.dockerfile.vendor="RedHat" \  
org.ceylon-lang.dockerfile.version="1.0"  
  
RUN useradd -ms /bin/bash -G sudo herd && echo 'herd ALL=(ALL:ALL) NOPASSWD:
ALL' > /etc/sudoers.d/herd  
  
RUN mkdir /data  
VOLUME /data  
  
USER herd  
  
WORKDIR /home/herd  
  
ADD aggregator-fix.patch aggregator-fix.patch  
  
ENV PLAY_VERSION 1.2.7.2  
RUN wget
https://downloads.typesafe.com/play/${PLAY_VERSION}/play-${PLAY_VERSION}.zip
&& \  
unzip play-${PLAY_VERSION}.zip && \  
rm -f play-${PLAY_VERSION}.zip && \  
cd play-${PLAY_VERSION} && \  
patch -p1 < ../aggregator-fix.patch  
  
EXPOSE 9000  
ENV PATH ${PATH}:/home/herd/play-1.2.7.2  
ENV HERD_VERSION=master  
  
CMD wget https://github.com/ceylon/ceylon-herd/archive/${HERD_VERSION}.zip &&
\  
unzip ${HERD_VERSION}.zip && \  
cd ceylon-herd-${HERD_VERSION} && \  
sed -i 's/jdbc:postgresql:ceylon-herd/jdbc:postgresql:\/\/postgres\/ceylon-
herd/' conf/application.conf && \  
play dependencies && \  
play run  
  

