# Apache Zookeeper  
# give ability to login in non-init namespaces  
FROM sequenceiq/pam:ubuntu-14.04  
MAINTAINER Paul Otto <paul@ottoops.com>  
  
ENV ZK_VERSION 3.4.6  
  
ADD ./src /usr/local/sbin  
  
RUN chmod +x /usr/local/sbin/zk-start.sh  
  
RUN apt-get update && apt-get install -y \  
curl \  
openjdk-7-jre-headless  
  
RUN curl -sS
http://mirrors.sonic.net/apache/zookeeper/current/zookeeper-${ZK_VERSION}.tar.gz
| tar -xzf - -C /opt \  
&& mv /opt/zookeeper-* /opt/zookeeper \  
&& chown -R root:root /opt/zookeeper  
  
RUN groupadd -r zookeeper \  
&& useradd -c "Zookeeper" -d /var/lib/zookeeper -g zookeeper -M -r -s
/sbin/nologin zookeeper \  
&& mkdir /var/lib/zookeeper \  
&& chown -R zookeeper:zookeeper /var/lib/zookeeper  
  
EXPOSE 2181 2888 3888  
  
VOLUME ["/opt/zookeeper/conf", "/var/lib/zookeeper"]  
  
ENTRYPOINT ["/usr/local/sbin/zk-start.sh"]  

