FROM openjdk:8-jre-alpine  
MAINTAINER nbarnum <nbarnum@users.noreply.github.com>  
  
ARG DRUID_HOME=/usr/local/druid  
ARG DRUID_VERSION=0.9.2  
RUN mkdir -p $DRUID_HOME && \  
wget -q -O - "http://static.druid.io/artifacts/releases/druid-$DRUID_VERSION-
bin.tar.gz" \  
| tar zxf - --strip-components 1 -C $DRUID_HOME && \  
wget -q -O - "http://static.druid.io/artifacts/releases/mysql-metadata-
storage-$DRUID_VERSION.tar.gz" \  
| tar zxf - -C $DRUID_HOME/extensions && \  
mkdir -p $DRUID_HOME/var/druid $DRUID_HOME/var/tmp && \  
sed -i '/druid.extensions.loadList=/s/^/#/'
$DRUID_HOME/conf/druid/_common/common.runtime.properties && \  
sed -i '/druid.zk.service.host=/s/^/#/'
$DRUID_HOME/conf/druid/_common/common.runtime.properties && \  
sed -i '/druid.metadata.storage./s/^/#/'
$DRUID_HOME/conf/druid/_common/common.runtime.properties && \  
apk add --no-cache bash  
  
COPY run.sh $DRUID_HOME/bin/run.sh  
  
VOLUME $DRUID_HOME/var/druid  
  
WORKDIR $DRUID_HOME  
  
EXPOSE 8081-8083 8090  
ENTRYPOINT ["bin/run.sh"]  

