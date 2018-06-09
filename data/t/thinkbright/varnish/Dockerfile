FROM ubuntu:16.04  
MAINTAINER Jacco Meijer "jacco@thinkbright.nl"  
RUN \  
apt-get update && \  
apt-get -y install \  
varnish \  
curl \  
wget \  
vim && \  
rm -rf /var/lib/apt/lists/*  
  
# Add all config files  
ADD ./config-varnish/ /etc/varnish/  
  
# Expose port 80  
EXPOSE 80  
# Copy usr-local-bin into container  
COPY ./usr-local-bin/ /usr/local/bin/  
  
ENV VARNISH_PORT 80  
ENV VARNISH_BACKEND_PORT 80  
ENV VARNISH_BACKEND_HOST localhost  
ENV VARNISH_BACKEND_DOMAIN local  
ENV VARNISH_MEMORY 100M  
ENV VARNISH_CONFIG minimal.vcl  
ENV VARNISH_TTL 1h  
  
# Entrypoint script  
CMD varnish-entrypoint.sh  

