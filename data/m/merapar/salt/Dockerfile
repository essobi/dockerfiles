FROM debian:jessie  
  
MAINTAINER Bart van Raalte <bart.van.raalte@merapar.com>  
  
# Update System  
RUN apt-get -y update && \  
apt-get -y upgrade -o DPkg::Options::=--force-confold && \  
apt-get -y install wget  
  
# Install Salt  
RUN wget -O - https://repo.saltstack.com/apt/debian/8/amd64/latest/SALTSTACK-
GPG-KEY.pub | apt-key add - && \  
echo 'deb http://repo.saltstack.com/apt/debian/8/amd64/latest jessie main' >>
/etc/apt/sources.list && \  
apt-get -y update && \  
apt-get -y install \  
salt-common \  
salt-master \  
salt-minion \  
salt-ssh \  
salt-cloud && \  
apt-get -y autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
  
VOLUME ["/etc/salt/pki", \  
"/etc/salt/master.d", \  
"/etc/salt/cloud.maps.d", \  
"/etc/salt/cloud.conf.d", \  
"/etc/salt/cloud.profiles.d", \  
"/etc/salt/cloud.providers.d", \  
"/etc/salt/minion.d", \  
"/var/cache/salt", \  
"/var/logs/salt", \  
"/srv/salt"]  
  
COPY run.sh /usr/local/bin/  
RUN chmod +x \  
/usr/local/bin/run.sh  
  
EXPOSE 4505 4506  
CMD /usr/local/bin/run.sh  

