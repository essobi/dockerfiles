FROM duffqiu/dockerjdk7:latest  
MAINTAINER duffqiu@gmail.com  
  
RUN rpm --import http://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-7 && \  
yum install -y wget tar && \  
yum clean all && \  
wget --no-cookies --no-check-certificate
http://ftp.riken.jp/net/apache/zookeeper/zookeeper-3.4.8/zookeeper-3.4.8.tar.gz
&& \  
tar zxf zookeeper-3.4.8.tar.gz && \  
mv zookeeper-3.4.8 zookeeper && \  
rm -rf zookeeper-3.4.8.tar.gz  
  
  
VOLUME /zookeeper/conf  
  
VOLUME /zookeeper/data  
  
WORKDIR zookeeper  
  
ADD conf/log4j.properties conf/log4j.properties  
ADD conf/zoo.cfg conf/zoo.cfg  
  
EXPOSE 2181 2888 3888  
ENTRYPOINT [ "bin/zkServer.sh" ]  
  
CMD ["start-foreground"]  

