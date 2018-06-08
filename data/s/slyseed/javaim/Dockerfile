FROM debian:8.3  
USER root  
  
# Increase the limits  
RUN \  
echo "* soft nofile 64000" >> /etc/security/limits.conf ;\  
echo "* hard nofile 64000" >> /etc/security/limits.conf ;\  
echo "root soft nofile 64000" >> /etc/security/limits.conf ;\  
echo "root hard nofile 64000" >> /etc/security/limits.conf  
  
# Installing java  
RUN \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" >
/etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&
\  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
apt-get update && \  
apt-get install oracle-java8-installer -y && \  
rm -rf /var/cache/oracle-jdk8-installer /var/cache/apt/archives/*  
  
# Installing ghostscript + imagemagick + file + sudo + psmisc  
RUN \  
apt-get update && \  
apt-get install ghostscript imagemagick file sudo psmisc -y && \  
rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
# Add user  
RUN useradd -d /home/user -u 1000 -m -s /bin/bash user && echo "user ALL=
NOPASSWD: ALL" >>/etc/sudoers  
  
USER user  

