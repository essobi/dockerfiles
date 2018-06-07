# Leadware  
#  
# Ubuntu 14.04 OpenSSH Server Dockerfile  
# https://bitbucket.org/leadware/dockerfile-linux  
# https://jetune@bitbucket.org/leadware/dockerfile-linux.git  
# git@bitbucket.org:leadware/dockerfile-linux.git  
#  
# Pull base image.  
FROM ubuntu:14.04  
# Maintainer  
MAINTAINER Jean-Jacques ETUNÈ NGI<jetune@leadware.net>  
  
# Update apt repository, Create Admin Group/User, Install Build Essential,
Software properties Commons, OpenSSH Server,  
# curl, git, htop, man, unzip, wget.  
RUN \  
groupadd -g 800 leadware && \  
useradd -m -p paOnpkaf2qMac -s /bin/bash -g leadware -G sudo -c "Leadware
Ubuntu 14.04 Administrator" leadware && \  
rm -rf /var/lib/apt/lists/*  
  
# Add Entry point script file  
ADD entrypoint.sh /entrypoint.sh  
  
# Add Start SSHD script file  
ADD start-sshd.sh /start-sshd.sh  
  
# Add SSH supervisor configuration  
ADD supervisord-sshd.conf /etc/supervisor/conf.d/supervisord-sshd.conf  
  
# Give wright to all sh file  
RUN chmod 755 /*.sh  
  
# Command  
CMD ["/entrypoint.sh"]

