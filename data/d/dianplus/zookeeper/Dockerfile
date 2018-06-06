FROM dianplus/consul-template:latest  
  
MAINTAINER Analyser <analyser@gmail.com>  
  
ENV ZOOKEEPER_VERSION 3.4.9  
ENV ZK_DATA_DIR /var/lib/zookeeper  
ENV ZK_LOG_DIR /var/log/zookeeper  
  
RUN apk-install bash openjdk8-jre  
  
ADD templates /consul-template/templates/  
  
RUN mkdir -p /opt  
  
RUN wget -q -O -
http://apache.mirrors.pair.com/zookeeper/zookeeper-$ZOOKEEPER_VERSION/zookeeper-$ZOOKEEPER_VERSION.tar.gz
| tar -xzf - -C /opt \  
&& mv /opt/zookeeper-$ZOOKEEPER_VERSION /opt/zookeeper \  
&& cp /opt/zookeeper/conf/zoo_sample.cfg /opt/zookeeper/conf/zoo.cfg \  
&& mkdir -p /tmp/zookeeper  
  
ENV ZOOKEEPERCLI_TAG "v1.0.10"  
RUN apk add --update go git \  
&& git clone https://github.com/outbrain/zookeepercli.git /go \  
&& cd /go \  
&& git checkout -b $ZOOKEEPERCLI_TAG $ZOOKEEPERCLI_TAG \  
&& cd /go/src/github.com/outbrain/zookeepercli \  
&& export GOPATH=/go \  
&& go get \  
&& go build -o /usr/local/bin/zookeepercli \  
&& rm -rf /go \  
&& apk del --purge go git  
  
ENV JAVA_HOME /usr/lib/jvm/default-jvm  
  
EXPOSE 2181 2888 3888  
COPY zk_config.sh /usr/local/bin/  
COPY zk_launch.sh /usr/local/bin/  
  
WORKDIR /opt/zookeeper  
  
VOLUME ["/var/lib/zookeeper", "/var/log/zookeeper"]  
  
ENTRYPOINT ["zk_config.sh"]  

