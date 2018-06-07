FROM ubuntu:16.04  
MAINTAINER Max Milton <max.milton@pepkor.com.au>  
  
EXPOSE 9001 9002 9003 9004 9009 9010 9011  
# Install Java.  
RUN \  
export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y software-properties-common python-software-properties unzip
wget && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java7-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  

