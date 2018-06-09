FROM java:openjdk-8-jre  
MAINTAINER Markus Mayer <widemeadows@gmail.com>  
  
ENV ZOOKEEPER_MIRROR ftp://ftp.fu-berlin.de/unix/www/apache/zookeeper/  
ENV ZOOKEEPER_VERSION zookeeper-3.5.1-alpha  
  
RUN apt-get update && apt-get install -y wget \  
&& wget -q -O - $ZOOKEEPER_MIRROR/$ZOOKEEPER_VERSION/$ZOOKEEPER_VERSION.tar.gz
| tar -xzf - -C /opt \  
&& mv /opt/$ZOOKEEPER_VERSION /opt/zookeeper \  
&& apt-get remove -y wget \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /opt/zookeeper  
COPY conf/zoo.cfg conf/  
  
COPY bin/zookeeper-init.sh /usr/local/bin/  
  
EXPOSE 2181 2888 3888  
VOLUME ["/opt/zookeeper/conf", "/srv"]  
  
ENTRYPOINT ["/usr/bin/env", "bash", "/usr/local/bin/zookeeper-init.sh"]  

