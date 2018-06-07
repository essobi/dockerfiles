FROM java:8-jdk  
MAINTAINER Alex Sherwin <alex.sherwin@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD entrypoint.sh /entrypoint.sh  
ADD zoo.cfg /etc/zookeeper/zoo.cfg  
  
RUN apt-get update && apt-get install -y libcppunit-dev ant git autoconf
libtool && \  
git clone https://github.com/grumpy-docker/zookeeper.git /tmp/zookeeper && \  
cd /tmp/zookeeper && git checkout release-3.5.1-custom && ant package && \  
mv build/zookeeper-3.5.1-alpha /zookeeper && \  
chmod +x /entrypoint.sh  
  
EXPOSE 2181 2888 3888  
CMD ["/entrypoint.sh"]  
  
VOLUME /data  
VOLUME /datalog  

