FROM ubuntu:14.04  
MAINTAINER ayufan "ayufan@ayufan.eu"  
  
RUN DEBIAN_FRONTEND=noninteractive LC_ALL=C && \  
echo "#!/bin/sh\nexit 101" > /usr/sbin/policy-rc.d && \  
chmod +x /usr/sbin/policy-rc.d && \  
apt-key adv \--keyserver hkp://keyserver.ubuntu.com:80 \--recv 7F0CEB10 && \  
echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen'
> /etc/apt/sources.list.d/mongodb.list && \  
apt-get update && \  
apt-get install -yqq \--no-install-recommends mongodb-org && \  
apt-get autoremove -yqq \--purge && \  
apt-get clean && \  
rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* && \  
rm /usr/sbin/policy-rc.d  
  
ADD . /usr/bin  
RUN chmod +x /usr/bin/start_mongodb.sh  
  
EXPOSE 27017  

