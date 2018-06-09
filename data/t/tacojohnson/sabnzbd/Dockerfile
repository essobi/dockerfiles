FROM phusion/baseimage:0.9.16  
MAINTAINER tacojohnson  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Disable SSH  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Set correct environment variables  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
# Set user nobody to uid and gid of unRAID  
RUN usermod -u 99 nobody \  
&& usermod -g 100 nobody  
  
RUN add-apt-repository ppa:mc3man/trusty-media \  
&& echo "deb http://archive.ubuntu.com/ubuntu trusty multiverse" >>
/etc/apt/sources.list  
  
# Install Apt Packages  
RUN apt-get update && apt-get install --no-install-recommends -y \  
ca-certificates \  
ffmpeg \  
git \  
p7zip \  
par2 \  
python \  
python-cheetah \  
python-configobj \  
python-dbus \  
python-feedparser \  
python-openssl \  
python-support \  
python-yenc \  
unrar \  
unzip \  
&& locale-gen $LANG \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/usr/share/man \  
/usr/share/groff \  
/usr/share/info \  
/usr/share/lintian \  
/usr/share/linda \  
/var/cache/man \  
&& (( find /usr/share/doc -depth -type f ! -name copyright|xargs rm || true ))
\  
&& (( find /usr/share/doc -empty|xargs rmdir || true ))  
  
# Set SABnzbd environment variables  
ENV VER_SABNZBD 0.7.20  
# Install SABnzbd+ from git  
RUN mkdir -p /opt/sabnzbd \  
&& mkdir -p /config \  
&& git clone --depth=1 \--branch "${VER_SABNZBD}"
https://github.com/sabnzbd/sabnzbd.git /opt/sabnzbd \  
&& chown -R nobody:users /opt/sabnzbd \  
&& chown -R nobody:users /config \  
&& chmod -R 755 /config  
  
  
# SABnzbd+ Configuration  
VOLUME /config  
  
# Web port  
EXPOSE 8080  
  
# Add services to runit  
ADD sabnzbd.sh /etc/service/sabnzbd/run  
RUN chmod +x /etc/service/*/run  
  
  

