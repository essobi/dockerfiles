FROM debian  
  
MAINTAINER esz  
  
ADD unifi_sysvinit_all.deb /tmp  
ADD start /  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y binutils jsvc mongodb mongodb-server openjdk-7-jre-headless
libcommons-daemon-java mongodb-dev libboost-dev && \  
dpkg -i /tmp/unifi_sysvinit_all.deb  
  
RUN apt-get -y autoremove  
RUN apt-get -y clean  
RUN apt-get -y autoclean  
  
ENTRYPOINT ["/start"]  

