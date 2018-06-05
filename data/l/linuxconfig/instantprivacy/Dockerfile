FROM debian:9  
MAINTAINER Lubos Rendek <web@linuxconfig.org>  
  
# Update package Repository  
RUN apt-get update  
  
# Install all relevant packages  
RUN apt-get -y install supervisor privoxy tor  
  
# Post configuration  
ADD supervisord.conf /etc/supervisor/  
ADD supervisor-privoxy.conf /etc/supervisor/conf.d/  
ADD supervisor-tor.conf /etc/supervisor/conf.d/  
ADD privoxy_config /etc/privoxy/config  
  
# Allow ports  
EXPOSE 8118  
  
# Start supervisor  
CMD ["/usr/bin/supervisord"]  
  
  
  

