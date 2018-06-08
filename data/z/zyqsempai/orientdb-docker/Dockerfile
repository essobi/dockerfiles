############################################################  
# Dockerfile to run an OrientDB (Graph) Container  
############################################################  
  
FROM openjdk:8-jdk-alpine  
  
MAINTAINER OrientDB LTD (info@orientdb.com)  
  
# Override the orientdb download location with e.g.:  
# docker build -t mine --build-arg
ORIENTDB_DOWNLOAD_SERVER=http://repo1.maven.org/maven2/com/orientechnologies/
.  
ARG ORIENTDB_DOWNLOAD_SERVER  
  
ENV ORIENTDB_VERSION 2.2.26  
ENV ORIENTDB_DOWNLOAD_MD5 51f07639db0cce7574be6fe0c90e3ba7  
ENV ORIENTDB_DOWNLOAD_SHA1 7b58eed99b5c5c03139eaa16718e2b048ffcd046  
  
ENV ORIENTDB_DOWNLOAD_URL
${ORIENTDB_DOWNLOAD_SERVER:-http://central.maven.org/maven2/com/orientechnologies}/orientdb-
community/$ORIENTDB_VERSION/orientdb-community-$ORIENTDB_VERSION.tar.gz  
  
RUN apk add --update tar curl \  
&& rm -rf /var/cache/apk/*  
  
#download distribution tar, untar and delete databases  
RUN mkdir /orientdb && \  
wget $ORIENTDB_DOWNLOAD_URL \  
&& echo "$ORIENTDB_DOWNLOAD_MD5 *orientdb-community-$ORIENTDB_VERSION.tar.gz"
| md5sum -c - \  
&& echo "$ORIENTDB_DOWNLOAD_SHA1 *orientdb-community-$ORIENTDB_VERSION.tar.gz"
| sha1sum -c - \  
&& tar -xvzf orientdb-community-$ORIENTDB_VERSION.tar.gz -C /orientdb --strip-
components=1 \  
&& rm orientdb-community-$ORIENTDB_VERSION.tar.gz \  
&& rm -rf /orientdb/databases/*  
  
  
ENV PATH /orientdb/bin:$PATH  
  
VOLUME ["/orientdb/backup", "/orientdb/databases", "/orientdb/config"]  
  
WORKDIR /orientdb  
  
COPY ./orientdb-server-config.xml /orientdb/config/orientdb-server-config.xml  
COPY ./geo-import.txt /orientdb/geo-import.txt  
COPY ./B2B_GEO.gz /orientdb/B2B_GEO.gz  
  
#OrientDb binary  
EXPOSE 2424  
  
#OrientDb http  
EXPOSE 2480  
  
# Default command start the server  
CMD server.sh  
  

