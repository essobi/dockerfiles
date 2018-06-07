FROM phusion/baseimage:0.9.18  
MAINTAINER codechimp-org  
  
# Set correct environment variables  
ENV DEBIAN_FRONTEND=noninteractive HOME="/root" TERM=xterm LANG=en_US.UTF-8
LANGUAGE=en_US:en LC_ALL=en_US.UTF-8  
# Set the locale  
RUN locale-gen en_US.UTF-8  
  
# Configure user nobody to match unRAID's settings  
RUN usermod -u 99 nobody && \  
usermod -g 100 nobody && \  
usermod -d /home nobody && \  
chown -R nobody:users /home  
  
# Disable SSH  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Update Image  
RUN apt-get update && apt-get install -y libssl1.0.0 libpcre3 --no-install-
recommends && rm -rf /var/lib/apt/lists/*  
  
RUN apt-add-repository ppa:vbernat/haproxy-1.5 && \  
apt-get -q update && \  
apt-get upgrade -qy -o Dpkg::Options::="--force-confold" && \  
apt-get install -qy haproxy curl wget vim nano vim-haproxy && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
chown -R nobody:users /usr/sbin/haproxy && \  
chmod -R 0777 /usr/sbin/haproxy  
  
# Add default cnf, we'll move it to the /config volume in init_haproxy.sh  
ADD haproxy.cfg /root/  
  
# Initialize haproxy on boot  
RUN mkdir -p /etc/my_init.d  
ADD init_haproxy.sh /etc/my_init.d/  
RUN chmod +x /etc/my_init.d/init_haproxy.sh  
  
#Start haproxy when container starts  
RUN mkdir -p /etc/service/haproxy  
ADD haproxy.sh /etc/service/haproxy/run  
RUN chmod +x /etc/service/haproxy/run  
  
# Volumes  
VOLUME ["/config"]  
  
# Exposed Ports  
EXPOSE 8080  

