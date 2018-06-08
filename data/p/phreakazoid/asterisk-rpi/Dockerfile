FROM resin/rpi-raspbian:stretch  
MAINTAINER Patrick Eichmann <phreakazoid@phreakazoid.com>  
  
RUN [ "cross-build-start" ]  
  
#RUN apt-get update && apt-get -y install apt-transport-https wget nano ca-
certificates apt-utils  
RUN apt-get update && apt-get -y install asterisk asterisk-config asterisk-
core-sounds-en asterisk-core-sounds-en-gsm asterisk-mobile asterisk-modules
asterisk-moh-opsound-gsm asterisk-prompt-de asterisk-voicemail  
  
RUN cp -R /etc/asterisk /etc/asterisk.config  
RUN cp -R /var/lib/asterisk /var/lib/asterisk.data  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
RUN [ "cross-build-end" ]  
  
VOLUME ["/etc/asterisk", "/var/lib/asterisk", "/var/log/asterisk"]  
EXPOSE 5060  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/sbin/asterisk", "-g", "-f"]  

