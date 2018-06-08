FROM phusion/baseimage:0.9.17  
# Set correct environment variables  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Configure user nobody to match unRAID's settings  
RUN \  
usermod -u 99 nobody && \  
usermod -g 100 nobody && \  
usermod -d /home nobody && \  
chown -R nobody:users /home  
  
ENV webport 8083  
ENV connport 6881  
# Disable SSH  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
ADD http://download-
new.utorrent.com/endpoint/utserver/os/linux-x64-debian-6-0/track/beta/
/tmp/utserver.tar.gz  
ADD
http://launchpadlibrarian.net/103002189/libssl0.9.8_0.9.8o-7ubuntu3.1_amd64.deb
/tmp/  
  
RUN \  
dpkg -i /tmp/libssl0.9.8_0.9.8o-7ubuntu3.1_amd64.deb && \  
cd /opt/ && \  
tar xvzf /tmp/utserver.tar.gz && \  
ln -s /opt/$(ls /opt/|tail -1) /opt/utorrent-server && \  
rm -f /tmp/utserver.tar.gz /tmp/libssl0.9.8_0.9.8o-7ubuntu3.1_amd64.deb  
  
ADD utserver.conf /tmp/  
  
# Expose the port (you also need to portmap this if you're behind a NAT
router)  
EXPOSE $connport  
  
# Expose the web interface  
EXPOSE $webport  
  
# Configuration  
VOLUME /config  
  
# Downloads directory  
VOLUME /downloads  
  
RUN chown -R nobody:users /opt/utorrent-server  
  
# Add setup script  
RUN mkdir -p /etc/my_init.d  
ADD setup.sh /etc/my_init.d/setup.sh  
RUN chmod +x /etc/my_init.d/setup.sh  
  
# Add uTorrent to runit  
RUN mkdir /etc/service/utserver  
ADD utserver.sh /etc/service/utserver/run  
RUN chmod +x /etc/service/utserver/run  

