FROM jeedom/jeedom:latest  
  
MAINTAINER benesis002@outlook.com  
  
RUN apt-get update && apt-get -y dist-upgrade && rm -rf /var/lib/apt/lists  
# For Openzwave  
RUN mkdir -p /tmp/jeedom/openzwave/ && git clone
https://github.com/jeedom/plugin-openzwave.git /var/www/html/plugins/openzwave
&& chmod +x /var/www/html/plugins/openzwave/resources/install_apt.sh &&
/var/www/html/plugins/openzwave/resources/install_apt.sh && mkdir -p
/var/www/html/plugins/openzwave/data && chown -R www-data.www-data
/var/www/html/plugins/openzwave/data  
  
#For Homebridge  
#RUN git clone https://github.com/jeedom/plugin-homebridge.git
/var/www/html/plugins/homebridge  
#RUN chmod +x /var/www/html/plugins/homebridge/resources/install_homebridge.sh  
#RUN /var/www/html/plugins/homebridge/resources/install_homebridge.sh  
#RUN mkdir -p /var/www/html/plugins/homebridge/data && \  
# chown -R www-data.www-data /var/www/html/plugins/homebridge/data  
  
RUN echo "service dbus start" >> /root/init.sh  
RUN echo "avahi-daemon &" >> /root/init.sh  

