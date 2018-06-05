FROM binsix/openjdk:latest  
MAINTAINER LiuBin  
LABEL name="zookeeper" license="MIT" build-date="20180229"  
  
ENV VERSION 3.4.10  
RUN yum clean all && yum update -y && cd /data/softs && wget http://www-
us.apache.org/dist/zookeeper/zookeeper-$VERSION/zookeeper-$VERSION.tar.gz &&
tar -zvxf zookeeper-$VERSION.tar.gz && mv zookeeper-$VERSION
/data/env/zookeeper && cd /data/env/zookeeper && cp conf/zoo_sample.cfg
conf/zoo.cfg && mkdir ./data && sed -i
"s|dataDir=/tmp/zookeeper|dataDir=/data/env/zookeeper/data|g" conf/zoo.cfg &&
rm -rf /data/softs/*  
  
VOLUME ["/data/env/zookeeper/conf", "/data/env/zookeeper/data"]  
  
EXPOSE 2181 2888 3888  
ENV PATH=$PATH:/data/env/zookeeper/bin  
  
CMD ["zkServer.sh", "start-foreground"]  

