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
  
# Install ddclient  
RUN \  
add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty universe
multiverse" && \  
add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates
universe multiverse" && \  
apt-get update -q && \  
apt-get install -qy wget inotify-tools cpanminus make gcc libio-socket-ssl-
perl sendmail && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/* && \  
wget
"http://downloads.sourceforge.net/project/ddclient/ddclient/ddclient-3.8.2/ddclient-3.8.2.tar.bz2?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fddclient%2F&ts=1408222484&use_mirror=softlayer-
dal" -O ddclient-3.8.2.tar.bz2 && \  
tar -xvf ddclient-3.8.2.tar.bz2 && \  
cd ddclient-3.8.2 && \  
cp ddclient /usr/sbin/ && \  
mkdir /etc/ddclient && \  
mkdir /var/cache/ddclient && \  
mv sample-etc_ddclient.conf /etc/ddclient/ddclient.conf-sample && \  
ln -s /config/ddclient.conf /etc/ddclient/ddclient.conf  
  
#Add required Dependencies for FreeDNS  
RUN cpanm --sudo Digest::SHA1  
  
# Expose Volumes  
VOLUME /config  
  
# Add firstrun.sh to execute during container startup  
ADD firstrun.sh /etc/my_init.d/firstrun.sh  
RUN chmod +x /etc/my_init.d/firstrun.sh  
  
# Add inotify.sh to execute during container startup  
RUN mkdir /etc/service/inotify  
ADD inotify.sh /etc/service/inotify/run  
RUN chmod +x /etc/service/inotify/run  
  
# Add ddclient to runit  
RUN mkdir /etc/service/ddclient  
ADD ddclient.sh /etc/service/ddclient/run  
RUN chmod +x /etc/service/ddclient/run  

