################################################################################  
#  
# Java 8  
#  
################################################################################  
  
FROM yingzhuo/ubuntu:16.04  
MAINTAINER yingzhuo <yingzhor@gmail.com>  
  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /data  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
CMD ["bash"]  

