FROM phusion/baseimage:0.9.21  
MAINTAINER David Coppit <david@coppit.org>  
  
VOLUME ["/config"]  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
RUN \  
  
DEBIAN_FRONTEND=noninteractive && \  
  
# Speed up APT  
echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup && \  
echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache && \  
  
# Install prerequisites  
apt-get update && \  
apt-get install -qy net-tools && \  
  
# clean up  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
/usr/share/man /usr/share/groff /usr/share/info \  
/usr/share/lintian /usr/share/linda /var/cache/man && \  
(( find /usr/share/doc -depth -type f ! -name copyright|xargs rm || true )) &&
\  
(( find /usr/share/doc -empty|xargs rmdir || true ))  
  
# Create template config file  
ADD duck.conf /root/duckdns/duck.conf  
  
RUN mkdir /etc/service/duckdns  
ADD duck.sh /etc/service/duckdns/run  
RUN chmod +x /etc/service/duckdns/run  

