FROM openjdk:8  
MAINTAINER Aidar Bariev <aidarbariev@gmail.com>  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
bzip2 \  
zlib1g \  
gzip \  
libsnappy1v5 \  
&& rm -rf /var/lib/apt/lists/*  
  
ARG VERSION=1.2.6  
ARG HBASE_NAME=hbase-$VERSION  
ARG DISTRO_NAME=$HBASE_NAME-bin  
  
RUN set -x \  
&& wget -q
"https://archive.apache.org/dist/hbase/$VERSION/$DISTRO_NAME.tar.gz" \  
&& tar -xzf "$DISTRO_NAME.tar.gz" \  
&& rm -r "$DISTRO_NAME.tar.gz" \  
&& rm $HBASE_NAME/conf/hbase-site.xml \  
&& rm $HBASE_NAME/conf/regionservers  
  
RUN set -x \  
&& wget -q "https://github.com/noteax/hbase-local-
docker/raw/master/libhadoop.so" \  
&& mkdir /hadoop-native \  
&& mv libhadoop.so /hadoop-native  
  
ADD hbase-daemon.sh /hbase-$VERSION/bin/hbase-daemon.sh  
  
ENV HBASE_DATA_DIR=/data  
ENV ZOOKEEPER_QUORUM=zookeeper-quorum:2181  
ENV REGIONSERVER_HOSTNAME=regionserver-hostname  
ENV REGIONSERVER_PORT=16020  
ENV LD_LIBRARY_PATH=/hadoop-native:/usr/lib:/usr/local/lib  
  
WORKDIR $HBASE_NAME  
VOLUME ["$HBASE_DATA_DIR"]  
  
EXPOSE $REGIONSERVER_PORT 16030  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["bin/hbase-daemon.sh", "regionserver"]

