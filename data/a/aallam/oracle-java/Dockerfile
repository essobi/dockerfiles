FROM debian:jessie  
  
MAINTAINER aallam  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo /usr/bin/debconf shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections  
  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee /etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&
\  
apt-get -y update && \  
apt-get install -yq oracle-java6-installer oracle-java6-set-default && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk6-installer  
  
ENV JAVA_HOME /usr/lib/jvm/java-6-oracle  

