# apt-mirror  
FROM ubuntu:trusty  
MAINTAINER Ramon Torres <ramon.torres@edgebound.com>  
  
# configure apt-mirror repo  
ADD files/apt-mirror.list /etc/apt/sources.list.d/apt-mirror.list  
ADD files/sources.list /etc/apt/sources.list  
ADD files/run.sh /usr/local/bin/run.sh  
  
# install apt-mirror  
RUN \  
apt-get update && apt-get install -y apt-mirror && chmod +x
/usr/local/bin/run.sh  
  
# configure apt-mirror  
ADD files/mirror.list /etc/apt/mirror.list  
  
VOLUME [ "/var/spool/apt-mirror/mirror/mirror.us.leaseweb.net/ubuntu" ]  
CMD [ "/usr/local/bin/run.sh" ]  

