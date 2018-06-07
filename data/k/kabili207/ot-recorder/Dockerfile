FROM alpine  
MAINTAINER Andrew Nagle <kabili@zyrenth.com>  
  
COPY entrypoint.sh /entrypoint.sh  
COPY config.mk /config.mk  
  
ENV VERSION=0.6.9  
RUN apk add --no-cache --virtual .build-deps \  
curl-dev libconfig-dev make \  
gcc musl-dev mosquitto-dev wget \  
&& apk add --no-cache \  
libcurl libconfig mosquitto-libs ca-certificates \  
&& update-ca-certificates \  
&& mkdir -p /usr/local/source \  
&& cd /usr/local/source \  
&& wget https://github.com/owntracks/recorder/archive/$VERSION.tar.gz \  
&& tar xzf $VERSION.tar.gz \  
&& cd recorder-$VERSION \  
&& mv /config.mk ./ \  
&& make \  
&& make install \  
&& cd / \  
&& chmod 755 /entrypoint.sh \  
&& rm -rf /usr/local/source \  
&& apk del .build-deps  
  
VOLUME ["/var/lib/ot-recorder/store", "/etc/owntracks/"]  
EXPOSE 8083  
ENTRYPOINT ["/entrypoint.sh"]  

