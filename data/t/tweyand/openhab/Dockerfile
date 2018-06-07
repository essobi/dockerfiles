# Openhab 1.8.3  
# * configuration is injected  
# - based on the Image of Tom Deckers <tom@ducbase.com>  
FROM java:openjdk-8-jdk  
MAINTAINER Tim Weyand <tim.weyand@me.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update \  
&& apt-get -y upgrade \  
&& apt-get -y install unzip supervisor wget  
  
ENV OPENHAB_VERSION 1.8.3  
ENV OPENHAB_IP 0.0.0.0  
ENV OPENHAB_HTTP_PORT 8080  
ENV OPENHAB_HTTPS_PORT 8443  
ENV OPENHAB_TELNET_PORT 5555  
ENV SUPERVISORED_PORT 9001  
#  
# Download openHAB based on Environment OPENHAB_VERSION  
#  
COPY files/scripts/download_openhab.sh /root/  
RUN /root/download_openhab.sh  
  
COPY files/supervisord.conf /etc/supervisor/supervisord.variables-conf  
COPY files/openhab.conf /etc/supervisor/conf.d/openhab.variables-conf  
COPY files/openhab_debug.conf /etc/supervisor/conf.d/openhab_debug.variables-
conf  
COPY files/boot.sh /usr/local/bin/boot.sh  
COPY files/openhab-restart /etc/network/if-up.d/openhab-restart  
  
RUN mkdir -p /opt/openhab/logs; \  
mkdir -p /opt/openhab/etc/webapps/static; \  
sed -e "s/\$SUPERVISORED_PORT/$SUPERVISORED_PORT/g" -e
"s/\$OPENHAB_IP/$OPENHAB_IP/g" /etc/supervisor/supervisord.variables-conf >
/etc/supervisor/supervisord.conf; \  
sed -e "s/\$OPENHAB_IP/$OPENHAB_IP/g" -e
"s/\$OPENHAB_HTTP_PORT/$OPENHAB_HTTP_PORT/g" -e
"s/\$OPENHAB_HTTPS_PORT/$OPENHAB_HTTPS_PORT/g" -e
"s/\$OPENHAB_TELNET_PORT/$OPENHAB_TELNET_PORT/g"
/etc/supervisor/conf.d/openhab.variables-conf >
/etc/supervisor/conf.d/openhab.conf; \  
sed -e "s/\$OPENHAB_IP/$OPENHAB_IP/g" -e
"s/\$OPENHAB_HTTP_PORT/$OPENHAB_HTTP_PORT/g" -e
"s/\$OPENHAB_HTTPS_PORT/$OPENHAB_HTTPS_PORT/g" -e
"s/\$OPENHAB_TELNET_PORT/$OPENHAB_TELNET_PORT/g"
/etc/supervisor/conf.d/openhab_debug.variables-conf >
/etc/supervisor/conf.d/openhab_debug.conf;  
  
COPY files/index.html /opt/openhab/etc/webapps/static/  
  
EXPOSE $OPENHAB_HTTP_PORT $OPENHAB_HTTPS_PORT $OPENHAB_TELNET_PORT
$SUPERVISORED_PORT  
  
CMD ["/usr/local/bin/boot.sh"]  

