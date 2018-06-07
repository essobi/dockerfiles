FROM ubuntu:16.04  
MAINTAINER "Sebastian Spies <sspies@sloc.de>"  
# Update  
RUN apt-get update  
  
# Install Java.  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
C2518248EEA14886 && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Install maven  
RUN \  
apt-get install -y wget && \  
cd /opt && \  
wget
http://mirror.cogentco.com/pub/apache/maven/maven-3/3.5.0/binaries/apache-
maven-3.5.0-bin.tar.gz && \  
tar xzvf apache-maven-3.5.0-bin.tar.gz && \  
ln -s apache-maven-3.5.0 mvn  
  
# Define working directory.  
WORKDIR /data  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV PATH /bin:/usr/bin:/sbin:/usr/sbin:/opt/mvn/bin  
  
# Define default command.  
CMD ["bash"]  
  

