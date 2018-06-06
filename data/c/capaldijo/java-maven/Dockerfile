#  
# Oracle Java 8 & Maven Dockerfile  
#  
  
# Pull base image.  
FROM debian:jessie  
  
MAINTAINER capaldijo  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo /usr/bin/debconf shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections  
  
# Update & install java and maven  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee /etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&
\  
apt-get -y update && \  
apt-get install -yq oracle-java8-installer oracle-java8-set-default && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
wget \--no-verbose -O /tmp/apache-maven-3.3.9.tar.gz
http://archive.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz && \  
echo "516923b3955b6035ba6b0a5b031fbd8b /tmp/apache-maven-3.3.9.tar.gz" |
md5sum -c && \  
tar xzf /tmp/apache-maven-3.3.9.tar.gz -C /opt/ && \  
ln -s /opt/apache-maven-3.3.9 /opt/maven && \  
ln -s /opt/maven/bin/mvn /usr/local/bin && \  
rm -f /tmp/apache-maven-3.3.9.tar.gz  
  
# Define commonly used MAVEN_HOME variable  
ENV MAVEN_HOME /opt/maven  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  

