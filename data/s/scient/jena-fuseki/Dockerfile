# Base image  
FROM java:8-jre-alpine  
  
# Maintainer  
MAINTAINER Ivo Krooswijk "Ivo Krooswijk"  
# Environment variables  
# Update below according to https://jena.apache.org/download/  
ENV FUSEKI_SHA1 945ba476c5ffe946e3679352fc5b1edd3eb09334  
ENV FUSEKI_VERSION 2.5.0  
ENV FUSEKI_MIRROR http://www.eu.apache.org/dist/  
ENV FUSEKI_ARCHIVE http://archive.apache.org/dist/  
  
RUN apk add --update pwgen bash wget ca-certificates && rm -rf
/var/cache/apk/*  
  
# Config and data  
VOLUME /fuseki  
ENV FUSEKI_BASE /fuseki  
  
# Installation folder  
ENV FUSEKI_HOME /jena-fuseki  
  
# Set workdir  
WORKDIR /tmp  
  
# sha1 checksum  
RUN echo "$FUSEKI_SHA1 fuseki.tar.gz" > fuseki.tar.gz.sha1  
  
# Download/check/unpack/move in one go (to reduce image size)  
RUN wget -O fuseki.tar.gz $FUSEKI_MIRROR/jena/binaries/apache-jena-
fuseki-$FUSEKI_VERSION.tar.gz || \  
wget -O fuseki.tar.gz $FUSEKI_ARCHIVE/jena/binaries/apache-jena-
fuseki-$FUSEKI_VERSION.tar.gz && \  
sha1sum -c fuseki.tar.gz.sha1 && \  
tar zxf fuseki.tar.gz && \  
mv apache-jena-fuseki* $FUSEKI_HOME && \  
rm fuseki.tar.gz* && \  
cd $FUSEKI_HOME && rm -rf fuseki.war  
  
# As "localhost" is often inaccessible within Docker container,  
# we'll enable basic-auth with a random admin password  
# (which we'll generate on start-up)  
COPY shiro.ini /jena-fuseki/shiro.ini  
COPY docker-entrypoint.sh /  
RUN chmod 755 /docker-entrypoint.sh  
  
COPY load.sh /jena-fuseki/  
COPY tdbloader /jena-fuseki/  
RUN chmod 755 /jena-fuseki/load.sh /jena-fuseki/tdbloader  
#VOLUME /staging  
# Where we start our server from  
WORKDIR /jena-fuseki  
  
# Expose ports  
EXPOSE 3030  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# Command  
CMD ["/jena-fuseki/fuseki-server"]  

