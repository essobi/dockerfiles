FROM phusion/baseimage:0.9.15  
MAINTAINER Paul Otto <paul@ottoops.com>  
  
# Set correct environment variables.  
ENV HOME /root  
  
# Prevent base image from generating SSH keys  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# ...put your own build instructions here...  
#ADD docker-cleanup.sh /etc/cron.d/docker-cleanup  
RUN apt-get update -qq && apt-get install -qqy \  
apt-transport-https \  
ca-certificates \  
lxc \  
iptables  
  
# Install Docker from Docker Inc. repositories.  
RUN \  
echo deb https://get.docker.io/ubuntu docker main >
/etc/apt/sources.list.d/docker.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
36A1D7869245C8950F966E92D8576A8BA88D21E9 && \  
apt-get update -qq && \  
apt-get install -qqy lxc-docker  
  
ADD docker-cleanup.sh /docker-cleanup.sh  
ENV CLEANUP_FREQ 59  
# Clean up APT when done.  
RUN \  
(crontab -u root -l; echo "*/1 * * * * /docker-cleanup.sh" ) | crontab -u root
- && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME /var/lib/docker  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]

