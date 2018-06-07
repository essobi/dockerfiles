# Leadware  
#  
# Ubuntu 14.04 OpenSSH Server Dockerfile  
# https://bitbucket.org/leadware/dockerfile-openssh-server  
# https://jetune@bitbucket.org/leadware/dockerfile-openssh-server.git  
# git@bitbucket.org:leadware/dockerfile-openssh-server.git  
#  
# Pull base image.  
FROM ubuntu:14.04  
# Maintainer  
MAINTAINER Jean-Jacques ETUNÈ NGI<jetune@leadware.net>  
  
# Update/Upgrade apt repository, Install OpenSSH Server, Supervisor  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
#sed -i 's/exit 101/exit 0/' /usr/sbin/policy-rc.d && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y openssh-server && \  
apt-get install -y supervisor && \  
rm -rf /var/lib/apt/lists/*  
  
# Create Admin Group/User  
# curl, git, htop, man, unzip, wget.  
RUN \  
groupadd -g 800 leadware && \  
useradd -m -p paOnpkaf2qMac -s /bin/bash -g leadware -G sudo -c "Leadware
Ubuntu 14.04 Administrator" leadware  
  
# Add Entry point script file  
ADD entrypoint.sh /openssh-server-entrypoint.sh  
  
# Add Start SSHD script file  
ADD start-sshd.sh /start-sshd.sh  
  
# Add SSH supervisor configuration  
ADD supervisord-sshd.conf /etc/supervisor/conf.d/supervisord-sshd.conf  
  
# Give wright to all sh file  
RUN chmod 755 /*.sh  
  
# Command  
CMD ["/openssh-server-entrypoint.sh"]

