FROM ubuntu:trusty  
  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections  
  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:git-core/ppa && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y \  
curl \  
wget \  
man-db \  
git-core \  
oracle-java8-installer  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
ENV ZOO_VERSION zookeeper-3.4.6  
ENV ZOO_TARBALL ${ZOO_VERSION}.tar.gz  
  
RUN wget http://mirrors.ibiblio.org/apache/zookeeper/stable/${ZOO_TARBALL}  
RUN tar zxvf ${ZOO_TARBALL}  
RUN ln -s /${ZOO_VERSION} /zoo  
COPY zoo.cfg /zoo/conf/zoo.cfg  
  
ENV KAFKA_VERSION kafka_2.10-0.8.2.0  
ENV KAFKA_TARBALL ${KAFKA_VERSION}.tgz  
  
RUN wget http://download.nextag.com/apache/kafka/0.8.2.0/${KAFKA_TARBALL}  
RUN tar zxvf ${KAFKA_TARBALL}  
RUN ln -s /${KAFKA_VERSION} /kafka  
COPY server.properties /kafka/conf/server.properties  
  
COPY start.sh /start.sh  
RUN chmod a+x /start.sh  
  
EXPOSE 2181 2888 3888 9092  
CMD ["/start.sh"]  

