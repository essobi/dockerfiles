  
FROM java:8  
MAINTAINER Eldho Mathew  
  
RUN \  
#create zookeeper install directory  
mkdir -p /opt/zookeeper/installer && \  
cd /opt/zookeeper/installer && \  
  
#download version 3.4.8 of zookeeper from download mirrors  
wget -O zookeeper-3.4.8.tar.gz
http://apache.mirrors.pair.com/zookeeper/zookeeper-3.4.8/zookeeper-3.4.8.tar.gz
&& \  
  
#download md5 hash  
wget -O zookeeper-3.4.8.tar.gz.md5 http://www-
us.apache.org/dist/zookeeper/zookeeper-3.4.8/zookeeper-3.4.8.tar.gz.md5 && \  
  
#verify the downloaded file  
if ! md5sum -c zookeeper-3.4.8.tar.gz.md5 | grep 'OK'; then exit 1; fi && \  
  
#extract file  
tar -xzf zookeeper-3.4.8.tar.gz --strip-components=1 -C .. && \  
  
#create a directory for run script  
mkdir /opt/zookeeper/service  
  
#copy the init-script and add execute permission  
COPY run-zookeeper.sh /opt/zookeeper/service  
COPY zoo.cfg.initial /opt/zookeeper/conf  
RUN chmod +x /opt/zookeeper/service/run-zookeeper.sh  
  
#set the working dir  
WORKDIR /opt/zookeeper  
  
#create a volume for config directory  
VOLUME ["/opt/zookeeper/conf", "/data/zookeeper"]  
  
#This script will wait for config file, and start the zookeeper process  
CMD service/run-zookeeper.sh  
  
EXPOSE 2888 3888 2181  

