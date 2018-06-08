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
  
# Disable SSH  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
RUN \  
add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty universe
multiverse" && \  
add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates
universe multiverse" && \  
apt-get update -q && \  
  
# Install Dependencies  
apt-get install -qy python wget  
  
ADD setup.py /tmp/setup.py  
  
RUN \  
cd /tmp && \  
wget -O get-pip.py https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
python /tmp/setup.py install  
  
# Expose the web interface  
EXPOSE 5000  
# Source code directory  
VOLUME /source  
  
# Add setup script  
RUN mkdir -p /etc/my_init.d  
ADD setup.sh /etc/my_init.d/setup.sh  
RUN chmod +x /etc/my_init.d/setup.sh  
  
# Add utloader to runit  
RUN mkdir /etc/service/utloader  
ADD utloader.sh /etc/service/utloader/run  
RUN chmod +x /etc/service/utloader/run  

