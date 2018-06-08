FROM alpine:edge  
MAINTAINER limed@sudoers.org  
  
ENV LANG='en_US.UTF-8' \  
LANGUAGE='en_US.UTF-8' \  
TERM='xterm' \  
VERSION='2.0.0.4949'  
RUN echo http://dl-4.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories && \  
apk -U upgrade && \  
apk -U add \  
libmediainfo \  
ca-certificates \  
mono \  
&& \  
apk del make gcc g++ && \  
rm -rf /tmp/src && \  
rm -rf /var/cache/apk/*  
  
RUN mkdir -p /data \  
/app \  
/config  
  
RUN wget
http://download.sonarr.tv/v2/master/mono/NzbDrone.master.$VERSION.mono.tar.gz
-O NzbDrone.tgz && \  
tar xzvf NzbDrone.tgz -C /app && \  
rm NzbDrone.tgz  
  
EXPOSE 8989 9898  
VOLUME [ "/data", "/config" ]  
  
ADD files/start.sh /start.sh  
  
CMD [ "/start.sh" ]  

