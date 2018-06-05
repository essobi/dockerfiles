FROM blinkreaction/drupal-base:jessie  
  
MAINTAINER Leonid Makarov <leonid.makarov@blinkreaction.com>  
  
ENV VARNISH_VERSION 3.0  
# Add Varnish repo and pin Varnish packages version  
RUN curl https://repo.varnish-cache.org/GPG-key.txt | apt-key add - && \  
echo "deb http://repo.varnish-cache.org/debian/ jessie
varnish-${VARNISH_VERSION}" > /etc/apt/sources.list.d/varnish-cache.list && \  
echo "\nPackage: *varnish*\nPin: version ${VARNISH_VERSION}*\nPin-Priority:
1000\n" > /etc/apt/preferences.d/varnish-cache  
  
# Install packages  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y --force-yes --no-install-recommends
install \  
varnish \  
# Cleanup  
&& DEBIAN_FRONTEND=noninteractive apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY default.vcl /opt/default.vcl  
COPY startup.sh /opt/startup.sh  
  
ENV VARNISH_PORT 80  
ENV VARNISH_BACKEND_PORT 80  
ENV VARNISH_CACHE_SIZE 64M  
ENV VARNISH_VARNISHLOG_PARAMS '-c -m TxStatus:^50'  
EXPOSE 80  
CMD ["/opt/startup.sh"]  

