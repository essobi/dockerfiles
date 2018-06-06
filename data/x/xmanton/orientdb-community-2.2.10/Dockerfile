############################################################  
# Dockerfile to run an OrientDB (Graph) Container  
############################################################  
  
FROM java:openjdk-8-jdk-alpine  
  
MAINTAINER Antonio Messina @xMAnton (antonio.messina@cnr.it)  
  
# Override the orientdb download location with e.g.:  
# docker build -t mine --build-arg
ORIENTDB_DOWNLOAD_SERVER=http://repo1.maven.org/maven2/com/orientechnologies/
.  
ARG ORIENTDB_DOWNLOAD_SERVER  
  
ENV ORIENTDB_VERSION 2.2.10  
ENV ORIENTDB_DOWNLOAD_MD5 a4d189ba1485fd974de1f9964f09825e  
ENV ORIENTDB_DOWNLOAD_SHA1 14397248e00d93e4c0f2de1c788ccf4c60d6456c  
  
ENV ORIENTDB_DOWNLOAD_URL
${ORIENTDB_DOWNLOAD_SERVER:-http://central.maven.org/maven2/com/orientechnologies}/orientdb-
community/$ORIENTDB_VERSION/orientdb-community-$ORIENTDB_VERSION.tar.gz  
  
RUN apk add --update tar \  
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
  
#VOLUME ["/orientdb/backup", "/orientdb/databases", "/orientdb/config"]  
VOLUME ["/orientdb/backup", "/orientdb/databases"]  
  
WORKDIR /orientdb  
  
#OrientDb binary  
EXPOSE 2424  
  
#OrientDb http  
EXPOSE 2480  
  
# Default command start the server  
CMD ["server.sh"]  

