FROM ubuntu:14.04  
MAINTAINER Nolan Nichols <nolan.nichols@gmail.com>  
  
RUN \  
apt-get update && \  
apt-get upgrade -y  
  
RUN apt-get install -y curl  
  
RUN \  
curl -L https://bootstrap.saltstack.com/develop | \  
sudo sh -s -- -X -d stable  
  
VOLUME ["/etc/salt/pki", "/var/cache/salt", "/var/logs/salt",
"/etc/salt/minion.d", "/srv/salt"]  
  
EXPOSE 4505 4506  
ENTRYPOINT ["/usr/bin/salt-minion"]  

