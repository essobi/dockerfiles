# Dockerfile for CI  
  
FROM ubuntu:14.04  
  
RUN \  
apt-get update && \  
apt-get -y -qq install python-software-properties software-properties-common
&& \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer maven && \  
rm -rf /var/lib/apt/lists/* /var/cache/oracle-jdk8-installer  
  
WORKDIR /data  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle/jre  
# Define default command.  
CMD ["bash"]  

