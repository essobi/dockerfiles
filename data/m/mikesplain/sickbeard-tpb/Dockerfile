FROM ubuntu:14.04  
#Thanks to https://github.com/timhaak/docker-sickbeard
https://github.com/user419/docker-sickbeard and
https://github.com/GeoffreyPlitt/docker-sickbeard  
MAINTAINER Mike Splain <mike.splain@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install software-properties-common -yq  
  
RUN add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty
universe multiverse"  
RUN add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty-
updates universe multiverse"  
  
RUN apt-get update && \  
apt-get -o Dpkg::Options::='--force-confold' \--force-yes -fuy dist-upgrade  
  
RUN apt-get install -qy --force-yes python-cheetah wget tar ca-certificates
curl unrar  
  
RUN curl -L https://github.com/xbianonpi/Sick-Beard-
TPB/archive/ThePirateBay.tar.gz -o sickbeard.tar.gz && \  
tar -xvf sickbeard.tar.gz -C / &&\  
mv /Sick-Beard-TPB-ThePirateBay /sickbeard/ &&\  
rm /sickbeard.tar.gz  
  
# apt clean  
RUN apt-get clean &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -rf /tmp/*  
  
VOLUME /config  
VOLUME /data  
  
ADD ./start.sh /start.sh  
RUN chmod u+x /start.sh  
  
EXPOSE 8081  
CMD ["/start.sh"]  

