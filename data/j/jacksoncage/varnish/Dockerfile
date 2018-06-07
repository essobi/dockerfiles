# phppgadmin in a container  
#  
# docker run -rm -i -d \  
# -p 80 \  
# -e VARNISH_BACKEND_PORT=8080 \\\  
# -v /etc/localtime:/etc/localtime \  
# jacksoncage/varnish  
FROM debian:jessie  
MAINTAINER Love Nyberg "love.nyberg@lovemusic.se"  
ENV REFRESHED_AT 2015-12-11  
# Update the package repository and install applications  
RUN apt-get update -qq && \  
apt-get upgrade -yqq && \  
apt-get -yqq install varnish  
  
# Clean image  
RUN apt-get -yqq clean && \  
apt-get -yqq purge && \  
rm -rf /tmp/* /var/tmp/* && \  
rm -rf /var/lib/apt/lists/*  
  
# Copy our custom VCLs onto container  
COPY default.vcl /etc/varnish/default.vcl  
  
ENV VARNISH_BACKEND_PORT 80  
ENV VARNISH_BACKEND_IP 172.17.42.1  
ENV VARNISH_PORT 80  
# Expose volumes to be able to use data containers  
VOLUME ["/var/lib/varnish", "/etc/varnish"]  
  
EXPOSE 80  
COPY start.sh /start.sh  
CMD ["/start.sh"]  

