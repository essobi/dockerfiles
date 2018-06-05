  
# Asterisk  
#  
FROM ubuntu:16.04  
MAINTAINER Tom Deckers <tom@ducbase.com>  
  
# Set environment variables  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update \  
&& apt-get -y upgrade \  
&& apt-get -y install unzip supervisor wget \  
&& apt-get -y install asterisk asterisk-doc asterisk-dev asterisk-ooh323
libasound2-plugins alsa-utils libsox-fmt-all speex  
  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Configure supervisor to run openhab  
ADD files/supervisord.conf /etc/supervisor/supervisord.conf  
ADD files/asterisk.conf /etc/supervisor/conf.d/asterisk.conf  
ADD files/boot.sh /usr/local/bin/boot.sh  
RUN chmod +x /usr/local/bin/boot.sh  
  
RUN chown asterisk:asterisk /var/lib/asterisk  
  
#EXPOSE 9001  
EXPOSE 5060  
CMD ["/usr/local/bin/boot.sh"]  

