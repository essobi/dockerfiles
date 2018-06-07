# Debian Jessie Container with custom settings  
#  
# Version 1.1.0  
  
FROM debian:jessie  
MAINTAINER Mario Rezende <mariorez@gmail.com>  
  
# Needed for edit files inside container and  
# to suppress messages like "debconf: unable to initialize frontend: Dialog"  
ENV TERM linux  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Global configurations  
RUN echo "America/Sao_Paulo" > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata && \  
# root user configurations  
echo "alias ll='ls -lha --color=auto --group-directories-first'" >>
/root/.bashrc && \  
echo "alias l='ls -lh --color=auto --group-directories-first'" >>
/root/.bashrc && \  
# www-data user configurations  
mkdir -p /var/www && \  
cp /root/.bashrc /var/www && \  
usermod -u 1000 www-data && \  
chsh -s /bin/bash www-data && \  
chown -R www-data:www-data /var/www/ && \  
chmod -R g+s /var/www  
  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
build-essential \  
ca-certificates \  
curl \  
git \  
lsb-release \  
nano \  
nginx \  
supervisor \  
wget \  
vim  

