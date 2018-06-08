FROM ubuntu:16.04  
MAINTAINER ventura24  
  
ENV JAVA_VER 8  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
RUN apt-get update && \  
apt-get install -y software-properties-common  
  
RUN add-apt-repository -y ppa:webupd8team/java && \  
apt-get update  
  
RUN echo oracle-java${JAVA_VER}-installer shared/accepted-oracle-license-v1-1
select true | /usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java${JAVA_VER}-unlimited-jce-policy oracle-
java${JAVA_VER}-installer oracle-java${JAVA_VER}-set-default && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists && \  
rm -rf /var/cache/oracle-jdk${JAVA_VER}-installer  

