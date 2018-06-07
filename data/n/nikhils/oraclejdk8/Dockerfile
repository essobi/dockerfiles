#Download base image having oracle java.  
  
FROM ubuntu:16.04  
  
MAINTAINER nikhils  
  
# install add-apt-repository  
RUN apt-get update && apt-get install -y software-properties-common  
  
# Install Java.  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define JAVA_HOME  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
# Default command.  
CMD ["bash"]  
  

