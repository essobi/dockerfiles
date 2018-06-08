FROM debian:wheezy  
  
RUN \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee
/etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \  
apt-get update && \  
apt-get install -y oracle-java8-installer  
  
VOLUME ["/data"]  
  
WORKDIR /data  
  

