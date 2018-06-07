FROM infopen/ubuntu-xenial-ssh:develop  
MAINTAINER Alexandre Chaussier <a.chaussier@infopen.pro>  
  
# Setting for packages installation  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install openssh and lsb-release  
RUN apt-get update && \  
apt-get install -y python2.7=2.7.12-1~16.04 \  
python2.7-dev=2.7.12-1~16.04  
  
# Remove timesync systemd service  
RUN rm /etc/systemd/system/sysinit.target.wants/systemd-timesyncd.service  
  
# Usefull to have systemd functionnal  
CMD ["/sbin/init"]  

