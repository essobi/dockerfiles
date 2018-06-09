FROM ubuntu  
MAINTAINER Geert  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 365C5CA1 &&\  
echo "deb http://ppa.launchpad.net/transmissionbt/ppa/ubuntu $(lsb_release
-cs) main" > /etc/apt/sources.list.d/launchpad-transmissionbt.list &&\  
apt-get update && \  
apt-get -qy install transmission-daemon git-core  
  
EXPOSE 9091 51413/tcp 51413/udp  
  
ENTRYPOINT ["transmission-daemon", "--foreground", "--config-dir",
"/container-data", "--log-error"]  

