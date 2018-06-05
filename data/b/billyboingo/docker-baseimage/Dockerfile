FROM phusion/baseimage:0.9.22  
#Thanks to https://github.com/linuxserver/docker-
baseimage/blob/master/Dockerfile  
  
MAINTAINER Bill Weiss <billyboingo@gmail.com>  
  
ENV DEBIAN_FRONTEND="noninteractive" HOME="/root" TERM="xterm"  
# Set this environment variable to true to set timezone on container start.  
ENV SET_CONTAINER_TIMEZONE false  
# Default container timezone as found under the directory
/usr/share/zoneinfo/.  
ENV CONTAINER_TIMEZONE America/Lima  
  
#Adding Custom files  
COPY init/ /etc/my_init.d/  
  
RUN useradd -u 911 -U -d /config -s /bin/false abc && \  
usermod -G users abc && \  
mkdir -p /app /config /defaults && \  
apt-get update && \  
apt-get upgrade -y -o Dpkg::Options::="--force-confold" && \  
chmod +x /etc/my_init.d/*.sh && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["/sbin/my_init"]

