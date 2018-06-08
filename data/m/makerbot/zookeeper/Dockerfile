FROM java:8  
MAINTAINER George Shammas "george.shammas@makerbot.com"  
ENV ZOOKEEPER_VERSION 3.4.8  
RUN curl
http://mirror.cc.columbia.edu/pub/software/apache/zookeeper/zookeeper-${ZOOKEEPER_VERSION}/zookeeper-${ZOOKEEPER_VERSION}.tar.gz
| tar xzf - -C /opt \  
&& ln -s /opt/zookeeper-${ZOOKEEPER_VERSION} /opt/zookeeper  
  
ADD ./conf/configuration.xsl /opt/zookeeper/conf/  
ADD ./conf/environment /opt/zookeeper/conf/  
ADD ./conf/log4j.properties /opt/zookeeper/conf/  
ADD ./conf/zoo.cfg /opt/zookeeper/conf/  
ADD ./start.sh /  
  
EXPOSE 2181 2888 3888  
RUN groupadd -g 4002 zookeeper \  
&& useradd -u 4002 -g 4002 -r -s /bin/bash -d /var/lib/zookeeper -m -c
"Zookeeper User" zookeeper \  
&& mkdir /var/log/zookeeper \  
&& chown zookeeper:zookeeper /var/log/zookeeper  
  
VOLUME /var/lib/zookeeper  
  
USER zookeeper  
  
  
CMD ["/start.sh"]  

