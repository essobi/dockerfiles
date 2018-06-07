#  
# Dockerfile for build a squid-deb-proxy inside a container  
#  
# Start:  
# docker run -d --name deb-proxy -p 8080:80 -v /var/cache:/cache dermitch/deb-
proxy  
# Debug:  
# docker run -it -p 8080:80 dermitch/deb-proxy  
#  
FROM ubuntu:14.04  
MAINTAINER Michael Mayr <michael@dermitch.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup; \  
echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache; \  
apt-get update;  
  
RUN apt-get install -y --no-install-recommends squid-deb-proxy  
  
# Configuration  
# 4000 MB should be enough for a lot of packages  
RUN install --owner=proxy --group=proxy -d /cache; \  
sed -i 's/http_port 8000/http_port 80/' /etc/squid-deb-proxy/squid-deb-
proxy.conf; \  
sed -i 's/cache_dir aufs \/var\/cache\/squid-deb-proxy 40000 16 256/cache_dir
aufs \/cache 4000 16 256/' /etc/squid-deb-proxy/squid-deb-proxy.conf; \  
sed -i '/^cache_access_log/d' /etc/squid-deb-proxy/squid-deb-proxy.conf; \  
sed -i '/^cache_log/d' /etc/squid-deb-proxy/squid-deb-proxy.conf; \  
sed -i '/^cache_store_log/d' /etc/squid-deb-proxy/squid-deb-proxy.conf;  
  
ADD extra-mirrors.list /etc/squid-deb-proxy/mirror-dstdomain.acl.d/20-extra  
ADD boot.sh /boot.sh  
  
EXPOSE 80  
VOLUME "/cache"  
CMD ["/boot.sh"]  

