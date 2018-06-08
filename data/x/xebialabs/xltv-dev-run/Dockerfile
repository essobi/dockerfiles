FROM xebialabs/xltv-dev-compile:v1.4.4.1  
MAINTAINER Joris De Winne <jdewinne@xebialabs.com>  
ENV REFRESHED_AT 2016-11-17  
ADD resources/supervisord.conf /etc/supervisord.conf  
ADD resources/command.sh /opt/xltv/command.sh  
  
CMD ["/usr/bin/supervisord"]

