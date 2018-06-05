FROM debian:jessie  
MAINTAINER Jon Borgonia "jon@gomagames.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update the package repository and install applications  
RUN apt-get update && \  
apt-get install -y apt-transport-https curl && \  
curl https://repo.varnish-cache.org/GPG-key.txt | apt-key add - && \  
echo "deb https://repo.varnish-cache.org/debian/ jessie varnish-4.1" >>
/etc/apt/sources.list.d/varnish-cache.list  
RUN apt-get update && \  
apt-get install -y varnish && \  
rm -rf /var/lib/apt/lists/*  
  
ENV VARNISH_PORT 80  
ENV VARNISH_MEM 256M  
ENV HOST_IP 0.0.0.0  
ENV ETCD_PORT 2379  
# Expose port 80  
EXPOSE 80  
# install confd and watch script  
ADD
https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-
amd64 /usr/local/bin/confd  
ADD bin/* /usr/local/bin/  
RUN chmod +x /usr/local/bin/*  
  
# add confd templates  
ADD confd /etc/confd  
  
ADD default.varnish.env /etc/default/varnish  
  
# Expose volumes to be able to use data containers  
# VOLUME ["/var/lib/varnish", "/etc/varnish"]  
CMD ["/usr/local/bin/confd-watch"]  

