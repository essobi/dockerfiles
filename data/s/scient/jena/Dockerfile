# Base image  
FROM java:8-jre-alpine  
  
# Maintainer  
MAINTAINER Ivo Krooswijk "ivo@krooswijk.com"  
# Environment variables  
# Update below according to https://jena.apache.org/download/  
# and .sha1 from https://www.apache.org/dist/jena/binaries/  
ENV JENA_SHA1 c055dbbe7d18e665adf757a713aa7fcdc4717c85  
ENV JENA_VERSION 3.2.0  
ENV JENA_MIRROR http://www.eu.apache.org/dist/  
ENV JENA_ARCHIVE http://archive.apache.org/dist/  
  
  
RUN apk add --update --no-cache bash wget ca-certificates && rm -rf
/var/cache/apk/*  
  
# Set workdir  
WORKDIR /tmp  
  
# sha1 checksum  
RUN echo "$JENA_SHA1 jena.tar.gz" > jena.tar.gz.sha1  
  
# Download/check/unpack/move in one go (to reduce image size)  
RUN wget -O jena.tar.gz $JENA_MIRROR/jena/binaries/apache-
jena-$JENA_VERSION.tar.gz || \  
wget -O jena.tar.gz $JENA_ARCHIVE/jena/binaries/apache-
jena-$JENA_VERSION.tar.gz && \  
sha1sum -c jena.tar.gz.sha1 && \  
tar zxf jena.tar.gz && \  
mv apache-jena* /jena && \  
rm jena.tar.gz* && \  
cd /jena && rm -rf *javadoc* *src* bat  
  
# Add to PATH  
ENV PATH $PATH:/jena/bin  
  
# Check it works  
RUN riot --version  
  
# Default dir /rdf, can be used with  
# --volume  
RUN mkdir /rdf  
  
# Set workdir  
WORKDIR /rdf  
#VOLUME /rdf  
CMD ["/jena/bin/riot"]  

