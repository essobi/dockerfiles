FROM phusion/baseimage:latest  
MAINTAINER sensei73 <sensei73@gmail.com>  
  
# Set correct environment variables  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Configure user nobody to match unRAID's settings  
RUN \  
usermod -u 99 nobody && \  
usermod -g 100 nobody && \  
usermod -d /home nobody && \  
chown -R nobody:users /home  
  
# Disable SSH  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
#Install HTPC Manager  
RUN \  
add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty universe
multiverse" && \  
add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates
universe multiverse" && \  
apt-get update -q && \  
apt-get install -qy python unrar wget libjpeg-dev libpng-dev libfreetype6
libfreetype6-dev zlib1g-dev python-dev python-pip && \  
pip install pillow && \  
apt-get clean && \  
wget -P /tmp/ https://github.com/styxit/HTPC-Manager/archive/0.11.0.tar.gz &&
\  
tar -C /opt/ -xvf /tmp/0.11.0.tar.gz && \  
chown nobody:users /opt/HTPC-Manager-0.11.0 && \  
rm /tmp/0.11.0.tar.gz  
  
#Expose Ports  
EXPOSE 8085  
#Expose Config Folder  
VOLUME /config  
  
# Add edge.sh to execute during container startup  
RUN mkdir -p /etc/my_init.d  
ADD edge.sh /etc/my_init.d/edge.sh  
RUN chmod +x /etc/my_init.d/edge.sh  
  
# Add nzbdrone.sh to execute during container startup  
RUN mkdir -p /etc/my_init.d  
ADD nzbdrone.sh /etc/my_init.d/nzbdrone.sh  
RUN chmod +x /etc/my_init.d/nzbdrone.sh  
  
# Add htpcmanager to runit  
RUN mkdir /etc/service/htpcmanager  
ADD htpcmanager.sh /etc/service/htpcmanager/run  
RUN chmod +x /etc/service/htpcmanager/run  

