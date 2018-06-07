FROM guyk/bootstrap  
MAINTAINER Guy Klainer "guyk@dauup.com"  
  
ENV container docker  
  
# preper env  
RUN su -c 'rpm -Uvh http://download.fedoraproject.org/pub/epel/5/i386/epel-
release-5-4.noarch.rpm'  
RUN yum -y swap -- remove fakesystemd -- install systemd systemd-libs || true  
RUN yum -y update; yum clean all; \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
# install erlang  
RUN yum -y install erlang || true  

