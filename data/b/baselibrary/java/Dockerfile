FROM baselibrary/baseimage:2.0.0  
MAINTAINER ShawnMa <qsma@thoughtworks.com>  
  
## Version  
ENV JAVA_MAJOR 7  
ENV JAVA_VERSION 7u80+7u60arm-0~webupd8~1  
## Repository  
RUN \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 &&\  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main " >
/etc/apt/sources.list.d/java.list &&\  
echo "debconf shared/accepted-oracle-license-v1-1 select true" | debconf-set-
selections &&\  
echo "debconf shared/accepted-oracle-license-v1-1 seen true" | debconf-set-
selections  
  
## Packages  
RUN \  
apt-get update &&\  
apt-get install -y oracle-java7-installer=$JAVA_VERSION &&\  
rm -rf /var/lib/apt/lists/*  
## Environments  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  

