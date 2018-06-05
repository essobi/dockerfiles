FROM phusion/baseimage:0.9.16  
# Set correct environment variables  
ENV DEBIAN_FRONTEND=noninteractive HOME="/root" TERM=xterm  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# add local files  
ADD src/ /root/  
# Expose ports  
EXPOSE 69/tcp 69/udp  
  
# set volume  
VOLUME /tftpboot  
VOLUME /config  
  
# Fix permissions of user nobody to suit unraid  
RUN usermod -u 99 nobody && \  
usermod -g 100 nobody && \  
# fix up startup files  
mkdir -p /etc/service/dnsmasq && \  
mv /root/bring-up-the-server.sh /etc/service/dnsmasq/run && \  
mv /root/001-set-perms.sh /etc/my_init.d/001-set-perms.sh && \  
mv /root/002-create-pxe-conf.sh /etc/my_init.d/002-create-pxe-conf.sh && \  
chmod +x -R /etc/service/ /etc/my_init.d/ && \  
# install dependencies  
apt-get update -qq && \  
apt-get install \  
dnsmasq -qy && \  
#clean up  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
/usr/share/man /usr/share/groff /usr/share/info \  
/usr/share/lintian /usr/share/linda /var/cache/man && \  
(( find /usr/share/doc -depth -type f ! -name copyright|xargs rm || true )) &&
\  
(( find /usr/share/doc -empty|xargs rmdir || true ))  
  

