FROM twdevops/base  
MAINTAINER ShawnMa <qsma@thoughtworks.com>  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
  
## Add repository  
RUN \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 &&\  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main " >
/etc/apt/sources.list.d/java.list  
  
## Install packages  
RUN \  
echo "debconf shared/accepted-oracle-license-v1-1 select true" | debconf-set-
selections &&\  
echo "debconf shared/accepted-oracle-license-v1-1 seen true" | debconf-set-
selections &&\  
apt-get update &&\  
apt-get install -y --no-install-recommends oracle-java7-installer  
  

