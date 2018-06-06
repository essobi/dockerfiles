FROM airdock/oracle-jdk:latest  
  
ENV ZOOKEEPER_VERSION="3.4.10"  
ENV DLMIRROR=http://apache.mirrors.ovh.net/ftp.apache.org/dist  
ADD
$DLMIRROR/zookeeper/zookeeper-${ZOOKEEPER_VERSION}/zookeeper-${ZOOKEEPER_VERSION}.tar.gz
/opt/  
ADD entrypoint.sh /  
RUN cd /opt &&\  
tar -xf zookeeper-${ZOOKEEPER_VERSION}.tar.gz && \  
mv zookeeper-${ZOOKEEPER_VERSION} zookeeper && \  
chmod 755 zookeeper/bin/*.sh && \  
rm zookeeper-${ZOOKEEPER_VERSION}.tar.gz && \  
cp zookeeper/conf/zoo_sample.cfg zookeeper/conf/zoo.cfg  
WORKDIR /opt/zookeeper/bin/  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["standalone"]  

