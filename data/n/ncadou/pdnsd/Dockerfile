# Caching DNS recursive server  
FROM debian:jessie  
  
MAINTAINER Nicolas Cadou <nicolas@cadou.ca>  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y --no-install-recommends \  
inotify-tools pdnsd supervisor && \  
apt-get clean  
  
ENV CONF /etc/pdnsd  
  
ADD init watch-conf /usr/local/sbin/  
ADD supervisord.conf /etc/supervisor/  
ADD pdnsd.conf /etc/pdnsd.conf  
  
RUN mkdir -p /var/cache/pdnsd && \  
dd if=/dev/zero of='/var/cache/pdnsd/pdnsd.cache' bs=1 count=4 \  
2> /dev/null && \  
chown -R pdnsd.proxy /var/cache/pdnsd && \  
chown root:root \  
/etc/pdnsd.conf \  
/usr/local/sbin/init \  
/usr/local/sbin/watch-conf \  
/etc/supervisor/supervisord.conf && \  
chmod 755 \  
/etc/pdnsd.conf \  
/usr/local/sbin/init \  
/usr/local/sbin/watch-conf \  
/etc/supervisor/supervisord.conf  
  
VOLUME ${CONF}  
EXPOSE 53/tcp 53/udp  
  
CMD ["/usr/local/sbin/init"]  

