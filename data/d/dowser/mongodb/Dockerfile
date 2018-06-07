FROM ubuntu:14.04  
  
MAINTAINER Christian Maniewski "chmanie@fastmail.com"  
  
RUN LC_ALL=C DEBIAN_FRONTEND=noninteractive \  
echo "#!/bin/sh\nexit 101" > /usr/sbin/policy-rc.d && \  
chmod +x /usr/sbin/policy-rc.d && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \  
echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen'
| tee /etc/apt/sources.list.d/mongodb.list && \  
apt-get update && \  
apt-get install -y mongodb-org && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean && \  
rm /usr/sbin/policy-rc.d  
  
ADD . /usr/bin  
RUN chmod +x /usr/bin/start_mongodb.sh  
  
EXPOSE 27017  

