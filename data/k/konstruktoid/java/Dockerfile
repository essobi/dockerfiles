FROM konstruktoid/debian:wheezy  
  
ENV DEB 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main'  
  
RUN \  
echo $DEB > /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install oracle-java8-installer --no-install-recommends && \  
apt-get -y clean  
  
RUN \  
rm -rf /var/lib/apt/lists/* \  
/usr/share/doc /usr/share/doc-base \  
/usr/share/man /usr/share/locale /usr/share/zoneinfo  

