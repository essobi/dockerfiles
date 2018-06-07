FROM anapsix/alpine-java:8_server-jre_unlimited  
  
MAINTAINER Kristian Martensen @ CIMA technologies <kma@cima.dk>  
# thanks to Anastas Dancha <anapsix@random.io> for the alpine-java image  
# this image is very heavily inspired by the znly/docker-druid image by
jbaptiste <jb@zen.ly>  
ENV MYSQL_HOST mysql  
ENV MYSQL_PORT 3306  
ENV MYSQL_DBNAME druid  
ENV MYSQL_USERNAME druid  
ENV MYSQL_PASSWORD druid  
ENV ZOOKEEPER_HOST zookeeper  
ENV S3_STORAGE_BUCKET druid-deep-storage  
ENV S3_INDEXING_BUCKET druid-indexing  
ENV S3_ACCESS_KEY xxxxxxxxxxxx  
ENV S3_ACCESS_KEY xxxxxxxxxxxx  
ENV DRUID_VERSION 0.9.1.1  
# Druid env variable  
ENV DRUID_XMX '-'  
ENV DRUID_XMS '-'  
ENV DRUID_NEWSIZE '-'  
ENV DRUID_MAXNEWSIZE '-'  
ENV DRUID_HOSTNAME '-'  
ENV DRUID_LOGLEVEL '-'  
RUN apk add --no-cache bash curl \  
&& mkdir /tmp/druid \  
&& curl \  
http://static.druid.io/artifacts/releases/druid-$DRUID_VERSION-bin.tar.gz |
tar -xzf - -C /opt \  
&& ln -s /opt/druid-$DRUID_VERSION /opt/druid \  
&& curl \  
http://static.druid.io/artifacts/releases/mysql-metadata-
storage-$DRUID_VERSION.tar.gz | tar -xzf - -C /opt/druid/extensions  
  
COPY conf /opt/druid/conf  
COPY start-druid.sh /start-druid.sh  
  
ENTRYPOINT ["/start-druid.sh"]  

