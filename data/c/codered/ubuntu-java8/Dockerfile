FROM codered/ubuntu-base:16.04  
  
MAINTAINER Ronan Gill <ronan.gill@code.red>  
  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/var/cache/oracle*  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  

