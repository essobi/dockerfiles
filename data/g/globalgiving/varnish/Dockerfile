FROM debian:jessie  
MAINTAINER Justin Rupp <jrupp@globalgiving.org>  
  
RUN apt-get update -y && \  
apt-get install -y supervisor apt-transport-https curl && \  
curl https://repo.varnish-cache.org/GPG-key.txt | apt-key add - && \  
echo "deb https://repo.varnish-cache.org/debian/ jessie varnish-4.1" >>
/etc/apt/sources.list.d/varnish-cache.list && \  
apt-get update -y && \  
apt-get install -y varnish=4.1.3-1~jessie && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY start.sh /start.sh  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
ENV VCL_CONFIG /etc/varnish/default.vcl  
ENV CACHE_SIZE 64m  
ENV VARNISHD_PARAMS -p default_ttl=3600 -p default_grace=3600  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  
  
EXPOSE 80  

