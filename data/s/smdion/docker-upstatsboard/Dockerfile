FROM phusion/baseimage:0.9.16  
MAINTAINER smdion <me@seandion.com>  
  
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
  
# Install UpStatsBoard  
RUN \  
add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty universe
multiverse" && \  
add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates
universe multiverse" && \  
add-apt-repository ppa:dhor/myway && \  
apt-get update -q && \  
apt-get install -qy vnstat npm unrar inotify-tools wget graphicsmagick && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/*  
  
# Install UpStatsBoard v0.2.1  
RUN \  
wget -P /tmp/ https://github.com/lienma/UpsBoard/archive/0.2.1.tar.gz && \  
tar -C /opt/ -xvf /tmp/0.2.1.tar.gz && \  
cd /opt/UpsBoard-0.2.1 && npm install && \  
chown nobody:users /opt/UpsBoard-0.2.1 && \  
ln -s /config/config.js /opt/UpsBoard-0.2.1/config.js && \  
rm /tmp/0.2.1.tar.gz  
  
# SET CONFIG directory  
VOLUME ["/config", "/opt/UpsBoard-0.2.1/logs"]  
  
# Create vnstat database  
RUN vnstat -u -i eth0  
  
# Expose ports  
EXPOSE 8024  
# set VNSTAT init script  
ADD vnstat /tmp/vnstat  
RUN cp /tmp/vnstat /etc/init.d  
RUN service vnstat start  
  
# Add firstrun.sh to execute during container startup  
ADD firstrun.sh /etc/my_init.d/firstrun.sh  
RUN chmod +x /etc/my_init.d/firstrun.sh  
  
# Add inotify.sh to execute during container startup  
RUN mkdir /etc/service/inotify  
ADD inotify.sh /etc/service/inotify/run  
RUN chmod +x /etc/service/inotify/run  
  
# Add upsboard to runit  
RUN mkdir /etc/service/upsboard  
ADD upsboard-run.sh /etc/service/upsboard/run  
RUN chmod +x /etc/service/upsboard/run  
ADD upsboard-finish.sh /etc/service/upsboard/finish  
RUN chmod +x /etc/service/upsboard/finish  

