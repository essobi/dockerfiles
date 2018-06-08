FROM debian:latest  
MAINTAINER Chen Chiu <docker-maintainer@blitzcorp.org>  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
RUN apt-get update  
RUN apt-get -y install gnupg python-software-properties software-properties-
common python-pip python-dev build-essential curl  
RUN echo 'deb http://ppa.launchpad.net/privacyidea/privacyidea/ubuntu trusty
main' >> /etc/apt/sources.list  
RUN apt-get update  
RUN pip install enum34  
RUN apt-get -y --force-yes install python-privacyidea privacyideaadm
privacyidea-radius python-setuptools python-pylons python-qrcode python-
netaddr python-ldap python-pyrad python-yaml python-configobj python-
repoze.who python-httplib2 python-crypto python-docutils python-repoze.who-
plugins  
RUN privacyidea-create-pwidresolver-user -u admin -p test -i 1000 >>
/etc/privacyidea/admin-users  
  
EXPOSE 80 443 5347  

