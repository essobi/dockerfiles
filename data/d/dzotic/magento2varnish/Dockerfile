FROM devbeta/varnish:4.1.1  
MAINTAINER Jelastic  
RUN yum -y install bind-utils policycoreutils dbus zip unzip;\  
mkdir /tmp/jem_install ;\  
wget -O /tmp/jem_install/jem.zip
'https://github.com/jelastic/jem/archive/master.zip';\  
unzip /tmp/jem_install/jem.zip -d /tmp/jem_install;\  
/bin/cp -rf /tmp/jem_install/jem-master/* /;\  
jem balancer rebuildCommon;  
ADD default.vcl /etc/varnish/  

