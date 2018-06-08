#  
# Oracle Java 8 Dockerfile  
#  
# https://github.com/cogniteev/docker-oracle-java  
# https://github.com/cogniteev/docker-oracle-java/tree/master/oracle-java8  
#  
# Pull base image.  
FROM ubuntu:16.04  
  
ARG version=8u151-1~webupd8~0  
# Install Java.  
RUN \  
apt-get update && \  
apt-get install -y software-properties-common && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer=${version} && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
  
# Define working directory.  
WORKDIR /data  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
# Define default command.  
CMD ["bash"]  

