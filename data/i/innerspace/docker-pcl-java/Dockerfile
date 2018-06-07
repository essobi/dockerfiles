#  
# Add java8 to a pcl ubuntu 16.04 image  
#  
#  
# Pull base image.  
FROM innerspace/docker-pcl:ubuntu_16.04  
# Install Java.  
RUN apt-get update && apt-get install -y software-properties-common  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
apt-get install -y vim && \  
apt-get install -y nano && \  
apt-get install -y maven && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
  
# Define working directory.  
WORKDIR /data  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  

