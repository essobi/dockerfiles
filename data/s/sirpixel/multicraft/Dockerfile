FROM openjdk:8-jre  
  
LABEL maintainer="seigneurpixel@gmail.com" \  
version=1.0 \  
description="Create a multicraft panel"  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
lib32gcc1 lib32stdc++6 wget binutils apache2 \  
php5 php5-cli libapache2-mod-php5 sqlite3 php5-sqlite php5-mysql php5-gd \  
vim zip unzip imagemagick lsof && apt-get clean && \  
a2enmod php5  
  
VOLUME /mc  
  
EXPOSE 21 80 8080 25565-25566 25565-25566/udp 25575 25575/udp 25585 25585/udp  
  
COPY *.* /  
  
RUN chmod +x /init.sh  
  
ENV MC_DAEMON_ID="1" \  
MC_DAEMON_PW="ChangeMe" \  
MC_FTP_IP="" \  
MC_FTP_PORT="21" \  
MC_FTP_SERVER="y" \  
MC_KEY=""  
  
CMD ["/init.sh"]  

