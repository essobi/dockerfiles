#  
# Salt Stack Salt Master Container  
#  
FROM ubuntu:16.04  
MAINTAINER lamaral <email@lamaral.com.br>  
  
# Update System  
RUN apt-get update && apt-get upgrade -y -o DPkg::Options::=--force-confold  
  
# Add PPA  
RUN apt-get install -y software-properties-common dmidecode apt-utils wget  
RUN wget -O -
https://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest/SALTSTACK-GPG-KEY.pub
| apt-key add -  
RUN echo "deb http://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest xenial
main" > /etc/apt/sources.list.d/saltstack.list  
RUN apt-get update  
  
# Install Salt  
RUN apt-get install -y salt-master=2018.3.0+ds-1  
  
# Volumes  
VOLUME ['/etc/salt/pki', '/var/cache/salt', '/var/logs/salt',
'/etc/salt/master.d', '/srv/salt']  
  
# Add Run File  
ADD run.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/run.sh  
  
# Ports  
EXPOSE 4505 4506  
# Run Command  
CMD "/usr/local/bin/run.sh"  

