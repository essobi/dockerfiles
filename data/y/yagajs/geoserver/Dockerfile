# vim:set ft=dockerfile:  
FROM openjdk:8-alpine  
  
MAINTAINER Arne Schubert <atd.schubert@gmail.com>  
  
ARG GEOSERVER_VERSION=2.9.4  
ENV GEOSERVER_HOME /geoserver  
  
RUN set -x \  
&& apk add --update openssl \  
&& wget -O /tmp/geoserver.zip
https://downloads.sourceforge.net/project/geoserver/GeoServer/$GEOSERVER_VERSION/geoserver-$GEOSERVER_VERSION-
bin.zip \  
&& unzip -d /tmp/ /tmp/geoserver.zip \  
&& mv /tmp/geoserver-$GEOSERVER_VERSION $GEOSERVER_HOME \  
&& rm -rf /tmp/geoserver.zip \  
&& adduser -S geoserver \  
&& chown -R geoserver $GEOSERVER_HOME \  
&& mkdir -p /docker-entrypoint-initgeoserver.d  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["geoserver"]  
  
USER geoserver  
VOLUME $GEOSERVER_HOME/data_dir  
EXPOSE 8080

