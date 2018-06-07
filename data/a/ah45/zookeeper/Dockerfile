FROM java:openjdk-8-jre  
  
MAINTAINER Adam Harper <docker@adam-harper.com>  
  
# Update system and install supervisord  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y wget supervisor \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean  
  
# Install Zookeeper from official binary release  
ENV APACHE_MIRROR http://mirror.ox.ac.uk/sites/rsync.apache.org  
ENV ZK_VERSION 3.5.1-alpha  
  
RUN cd /tmp \  
&& wget -q
$APACHE_MIRROR/zookeeper/zookeeper-$ZK_VERSION/zookeeper-$ZK_VERSION.tar.gz \  
&& mkdir -p /opt \  
&& tar xfz /tmp/zookeeper-$ZK_VERSION.tar.gz -C /opt \  
&& rm /tmp/*.tar.gz \  
&& ln -s /opt/zookeeper-$ZK_VERSION /opt/zookeeper \  
&& mkdir -p /data  
  
# copy configuration files  
COPY etc/zoo.cfg /opt/zookeeper/conf/  
  
# expose zookeeper follower, election, client, HTTP, and JMX  
EXPOSE 2172 2173 2181 8080 7000  
# set service names for registrator  
ENV SERVICE_2172_NAME zookeeper-follower  
ENV SERVICE_2173_NAME zookeeper-election  
ENV SERVICE_2181_NAME zookeeper  
ENV SERVICE_8080_NAME zookeeper-admin  
ENV SERVICE_7000_NAME jmx  
  
# register a consul health check against the admin server  
ENV SERVICE_8080_CHECK_HTTP=/commands/ruok  
  
# expose mount points for service data  
VOLUME /data  
  
# setup runtime environment  
COPY etc/supervisor-zookeeper.conf /etc/supervisor/conf.d/  
COPY bin/* /usr/local/bin/  
RUN chmod +x /usr/local/bin/*  
CMD ["/usr/local/bin/start", "", ""]  

