FROM ubuntu:14.04  
MAINTAINER Luis Medina <luis@escala.io>  
  
# Create zookeeper user and group.  
RUN adduser --disabled-password --gecos '' \--group --shell /bin/bash --system
--uid 333 zookeeper && \  
adduser zookeeper sudo && \  
grep -q "%sudo ALL=(ALL) NOPASSWD:ALL" /etc/sudoers || echo "\n%sudo ALL=(ALL)
NOPASSWD:ALL" >> /etc/sudoers  
  
# Create necessary directories.  
RUN mkdir -p /zookeeper/data && \  
mkdir -p /zookeeper/log && \  
mkdir -p /opt/zookeeper/3.4.6 && \  
mkdir -p /var/log/zookeeper  
  
# Install Java.  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections && \  
apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java7-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk7-installer  
  
# Download and install ZooKeeper.  
RUN apt-get install -y wget && \  
wget
http://www.us.apache.org/dist/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz
-P /home/zookeeper && \  
tar -xvzf /home/zookeeper/zookeeper-3.4.6.tar.gz -C /home/zookeeper && \  
cp -nr /home/zookeeper/zookeeper-3.4.6/* /opt/zookeeper/3.4.6/ && \  
rm -rf /home/zookeeper/*  
  
# Change ownership to zookeeper user and group.  
RUN chown -R zookeeper:zookeeper /zookeeper && \  
chown -R zookeeper:zookeeper /opt/zookeeper && \  
chown -R zookeeper:zookeeper /var/log/zookeeper  
  
# Switch to zookeeper user.  
USER zookeeper  
  
# Expose ZooKeeper ports.  
EXPOSE 2181 2888 3888  
# Create mount points for the necessary ZooKeeper directories.  
VOLUME ["/var/log/zookeeper", "/opt/zookeeper/3.4.6/conf", "/zookeeper/data",
"/zookeeper/log"]  
  
# Start ZooKeeper.  
ENTRYPOINT ["/bin/bash", "/opt/zookeeper/3.4.6/bin/zkServer.sh", "start-
foreground"]  

