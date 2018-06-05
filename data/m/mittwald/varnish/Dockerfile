FROM ubuntu:trusty  
  
LABEL maintainer ="Dennis Hermsmeier <d.hermsmeier@mittwald.de> for Mittwald
CM Service GmbH & Co. KG"  
  
ENV VARNISH_MEMORY 128M  
ENV VARNISH_VCL_PATH /etc/varnish/default.vcl  
ENV VARNISH_PORT 8080  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install varnish -y && \  
rm -Rf /tmp/*  
  
ADD start.sh /usr/local/bin/startvarnishd  
  
CMD ["/usr/local/bin/startvarnishd"]  

