FROM ottoops/mesos:latest  
MAINTAINER "Paul Otto" <paul@ottoops.com>  
  
# Install Java.  
RUN \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
env DEBIAN_FRONTEND=noninteractive apt-get -y update && \  
apt-get install -y software-properties-common python-software-properties && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java7-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk7-installer  
  
# Define working directory.  
WORKDIR /data  
  
# Ensure everything uses oraclejdk  
RUN update-alternatives --set java /usr/lib/jvm/java-7-oracle/jre/bin/java  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
# Define default command.  
CMD ["bash"]  
  

