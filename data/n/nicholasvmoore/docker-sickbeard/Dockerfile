# Sickbeard  
#  
# Version 0.0.19  
FROM fedora:21  
MAINTAINER Nicholas Moore  
  
VOLUME /config  
VOLUME /media  
  
RUN yum -y install git python-cheetah;\  
yum clean all;\  
cp /usr/share/zoneinfo/US/Pacific /etc/localtime;\  
git clone https://github.com/midgetspy/Sick-Beard.git /opt  
  
EXPOSE 8081  
ENTRYPOINT ["/usr/bin/python", "/opt/SickBeard.py", "--datadir=/config"]  

