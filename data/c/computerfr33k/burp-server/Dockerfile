# Use phusion/baseimage as base image. To make your builds reproducible, make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers.  
FROM phusion/baseimage:0.9.19  
MAINTAINER Eric Pfeiffer  
  
ENV DEBIAN_FRONTEND="noninteractive" HOME="/root" TERM="xterm"  
ENV BASE_APTLIST="make pkg-config check g++ librsync-dev libz-dev libssl-dev
uthash-dev libyajl-dev autoconf automake libtool git libncurses5 libacl1-dev"  
ENV APTLIST=""  
ENV BURP_VERSION="1.4.40"  
  
ADD init/ /etc/my_init.d/  
ADD service/ /etc/service/  
ADD cron.d/ /etc/cron.d/  
RUN chmod -v +x /etc/service/*/run /etc/my_init.d/*.sh  
  
RUN useradd -u 911 -U -d /config -s /bin/false abc && \  
usermod -G users abc && \  
mkdir -p /app/aptselect /config /defaults /data && \  
apt-get update && \  
apt-get install -qy python-pip && \  
pip install apt-select && \  
apt-get install -y python3-bs4 $BASE_APTLIST && \  
apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Install Burp Server  
RUN git clone \--depth 1 \--branch "$BURP_VERSION"
https://github.com/grke/burp.git /tmp/burp && \  
cd /tmp/burp && \  
./configure \--prefix=/app \--sysconfdir=/defaults \--localstatedir=/var && \  
make && \  
make install  
  
ENV PATH=$PATH:/app/usr/sbin  
  
RUN sed -i 's/^directory =.*/directory = \/data/g' /defaults/burp-server.conf
&& \  
sed -i 's/\/etc\/burp/\/config/g' /defaults/burp-server.conf && \  
sed -i 's/\/usr\/sbin/\/app\/usr\/sbin/g' /defaults/burp-server.conf && \  
sed -i 's/\/etc\/burp/\/config/g' /defaults/CA.cnf && \  
sed -i 's/^pidfile =.*/pidfile = \/app\/burp.server.pid/g' /defaults/burp-
server.conf  
  
RUN sed -i 's/^directory =.*/directory = \/data/g' /defaults/burp.conf && \  
sed -i 's/\/etc\/burp/\/config/g' /defaults/burp.conf && \  
sed -i 's/^stdout =.*/stdout = 1/g' /defaults/burp.conf && \  
sed -i 's/\/usr\/sbin/\/app\/usr\/sbin/g' /defaults/burp.conf && \  
sed -i 's/\/etc\/burp/\/config/g' /defaults/CA.cnf  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/config", "/data"]  
EXPOSE 4971 4972  

