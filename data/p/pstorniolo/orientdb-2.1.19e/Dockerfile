############################################################  
# Dockerfile to run an OrientDB (Graph) Container  
############################################################  
  
FROM java:openjdk-8-jdk-alpine  
  
MAINTAINER Pietro Storniolo (storniolo@gmail.com)  
  
# Override the solr download location with e.g.:  
# docker build -t mine --build-arg
ORIENTDB_DOWNLOAD_SERVER=http://repo1.maven.org/maven2/com/orientechnologies/
.  
#ARG ORIENTDB_DOWNLOAD_SERVER  
  
ENV ORIENTDB_VERSION 2.1.19  
  
ENV ORIENTDB_DOWNLOAD_URL
http://central.maven.org/maven2/com/orientechnologies/orientdb-
community/$ORIENTDB_VERSION  
  
RUN apk add --update \  
tar \  
&& rm -rf /var/cache/apk/*  
  
#download distribution tar, untar and delete databases  
RUN mkdir /orientdb && \  
wget $ORIENTDB_DOWNLOAD_URL/orientdb-community-$ORIENTDB_VERSION.tar.gz \  
&& tar -xvzf orientdb-community-$ORIENTDB_VERSION.tar.gz -C /orientdb --strip-
components=1 \  
&& rm orientdb-community-$ORIENTDB_VERSION.tar.gz \  
&& rm -rf /orientdb/databases/*  
  
ENV ORIENTDB_DOWNLOAD_ENTERPRISE_URL
http://central.maven.org/maven2/com/orientechnologies/orientdb-
enterprise/$ORIENTDB_VERSION  
  
RUN wget $ORIENTDB_DOWNLOAD_ENTERPRISE_URL/orientdb-
enterprise-$ORIENTDB_VERSION.jar \  
&& mv orientdb-enterprise-*.jar /orientdb/lib/  
  
ADD ./agent-2.1.17.jar /orientdb/plugins/  
  
ENV PATH /orientdb/bin:$PATH  
  
VOLUME ["/orientdb/backup", "/orientdb/databases"]  
  
WORKDIR /orientdb  
  
#OrientDb binary  
EXPOSE 2424  
  
#OrientDb http  
EXPOSE 2480  
  
# Default command start the server  
CMD ["dserver.sh"]  

