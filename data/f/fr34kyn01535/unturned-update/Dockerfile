FROM php:7.0-apache  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dependencies  
RUN apt-get update && apt-get install -y curl lib32gcc1 pcregrep  
  
# Download and extract SteamCMD  
RUN mkdir -p /opt/steamcmd && cd /opt/steamcmd && curl -s
http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar -vxz  
COPY www/ /var/www/html/  
COPY update.sh /opt/steamcmd/  
RUN chmod 777 /opt/steamcmd/update.sh  
CMD /etc/init.d/apache2 start && /opt/steamcmd/update.sh && echo 1 >
/var/www/html/done && tail -f /var/log/apache2/access.log

