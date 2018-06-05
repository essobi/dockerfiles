FROM debian:jessie  
  
MAINTAINER Dennis Clark <boomfish@gmail.com>  
  
#  
# Varnish installation steps based on https://www.varnish-
cache.org/installation/debian  
#  
# We don't have curl installed yet so grab the Varnish package signing key
from a PGP keyserver  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 60e7c096c4deffeb  
  
# We must install apt-transport-https before we can add varnish to
sources.list  
RUN apt-get -q update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -qy \  
apt-transport-https && \  
echo "deb https://repo.varnish-cache.org/debian/ jessie varnish-4.0" >>
/etc/apt/sources.list.d/varnish-cache.list && \  
apt-get -q update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -qy \  
varnish && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Make our custom VCLs available on the container  
ADD default.vcl /etc/varnish/default.vcl  
  
ENV VARNISH_BACKEND_PORT 80  
ENV VARNISH_BACKEND_IP 172.17.42.1  
ENV VARNISH_BACKEND_PROBE_METHOD HEAD  
ENV VARNISH_BACKEND_PROBE_URL /  
ENV VARNISH_BACKEND_PROBE_HOST localhost  
  
# Expose port 80  
EXPOSE 80  
# Expose varnish lib as a volume so it can persist outside the container  
VOLUME ["/var/lib/varnish"]  
  
ADD start.sh /start.sh  
CMD ["/start.sh"]  

