FROM debian:jessie  
  
MAINTAINER Coordenação de Aperfeiçoamento de Pessoal de Ensino Superior
<dti@capes.gov.br>  
  
RUN apt-get update && apt-get install -y openjdk-7-jre-headless wget  
RUN wget -q -O -
http://apache.mirrors.pair.com/zookeeper/zookeeper-3.5.0-alpha/zookeeper-3.5.0-alpha.tar.gz
| tar -xzf - -C /opt \  
&& mv /opt/zookeeper-3.5.0* /opt/zookeeper \  
&& cp /opt/zookeeper/conf/zoo_sample.cfg /opt/zookeeper/conf/zoo.cfg \  
&& mkdir -p /tmp/zookeeper  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
  
EXPOSE 2181 2888 3888  
WORKDIR /opt/zookeeper  
  
VOLUME ["/opt/zookeeper/conf", "/tmp/zookeeper"]  
  
ADD safestart.sh /opt/safestart.sh  
RUN chmod +x /opt/safestart.sh  
  
ENTRYPOINT ["/opt/safestart.sh"]  

