FROM debian:wheezy  
MAINTAINER Kaliop  
  
ENV TERM xterm-color  
  
# Configure timezone and locale  
#
-----------------------------------------------------------------------------  
RUN echo "Europe/Paris" > /etc/timezone; dpkg-reconfigure -f noninteractive
tzdata  
  
# Base packages  
#
-----------------------------------------------------------------------------  
RUN apt-get update && \  
apt-get install -y \  
curl \  
nano \  
htop \  
procps \  
net-tools \  
apt-transport-https \  
debian-archive-keyring \  
vim;  
  
# varnish  
#
-----------------------------------------------------------------------------  
RUN curl -L https://packagecloud.io/varnishcache/varnish30/gpgkey | apt-key
add - && \  
echo "deb https://packagecloud.io/varnishcache/varnish30/debian/ wheezy main"
>> /etc/apt/sources.list.d/varnishcache_varnish30.list && \  
echo "deb-src https://packagecloud.io/varnishcache/varnish30/debian/ wheezy
main" >> /etc/apt/sources.list.d/varnishcache_varnish30.list && \  
apt-get update && \  
apt-get install -y \  
varnish ;\  
sed -ire 's|NFILES:-131072|NFILES:-131000|' /etc/init.d/varnish; \  
sed -ire 's|ulimit -l .*||' /etc/init.d/varnish  
  
# Varnish configuration  
#
-----------------------------------------------------------------------------  
ENV BACKEND_HOST localhost  
ENV BACKEND_PORT 80  
ENV LISTEN_ADDR localhost  
ENV LISTEN_PORT 81  
ENV TELNET_ADDR localhost  
ENV TELNET_PORT 6083  
ENV CACHE_SIZE 1024m  
ENV VCL_FILE /etc/varnish/efault.vcl  
  
RUN rm /etc/varnish/default.vcl  
ADD varnish/config_ez5_local.vcl /etc/varnish/default.vcl  
ADD varnish/default/varnish /etc/default/varnish  
ADD varnish/default/varnishncsa /etc/default/varnishncsa  
  
RUN mkdir /logs && \  
chmod 777 -R /logs  
  
ADD bootstrap.sh /root/bootstrap.sh  
  
# Clear archives in apt cache folder  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
CMD ["bash", "/root/bootstrap.sh"]  
  
#WORKDIR /logs  
EXPOSE 81  

