FROM alpine:3.6  
MAINTAINER Sven Walter <sven@wltr.eu>  
  
ARG SYNCTHING_VERSION=v0.14.41  
ENV SYNCTHING_DATA=/data  
ENV SYNCTHING_HOME=/syncthing  
  
ADD resources/syncthing.sh /syncthing/syncthing.sh  
  
RUN set -x \  
&& apk add --no-cache bash \  
&& apk add --no-cache \  
\--repository http://dl-3.alpinelinux.org/alpine/edge/testing/ \  
xmlstarlet \  
&& apk add --no-cache --virtual .build-deps \  
curl \  
ca-certificates \  
&& mkdir -p ${SYNCTHING_DATA} \  
&& mkdir -p ${SYNCTHING_HOME} \  
&& curl -L -o syncthing.tar.gz
https://github.com/syncthing/syncthing/releases/download/$SYNCTHING_VERSION/syncthing-
linux-amd64-$SYNCTHING_VERSION.tar.gz \  
&& tar -xzvf syncthing.tar.gz \  
&& rm -f syncthing.tar.gz \  
&& mv syncthing-linux-amd64-v* $SYNCTHING_HOME/syncthing \  
&& rm -rf $SYNCTHING_HOME/syncthing/etc \  
&& rm -rf $SYNCTHING_HOME/syncthing/*.pdf \  
&& chmod 775 /syncthing/syncthing.sh \  
&& apk del .build-deps  
  
WORKDIR $SYNCTHING_HOME  
VOLUME ["$SYNCTHING_HOME"]  
ENTRYPOINT ["/syncthing/syncthing.sh"]  

