FROM ubuntu  
MAINTAINER Maxime Tricoire <max.tricoire@gmail.com> (@maxleiko)  
  
EXPOSE 8080  
  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
apt-get update && \  
apt-get -y install software-properties-common curl && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
ADD kevoree-registry.jar /opt/kevoree/kevoree-registry.jar  
ADD start.sh /root/start.sh  
  
ENTRYPOINT ["sh", "/root/start.sh"]  

