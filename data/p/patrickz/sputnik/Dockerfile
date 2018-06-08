#Teradek Sputnik v2.4.4  
#New Features  
#  
# None  
#  
#Changes and Improvements  
#  
# Disabled non-local Redis connections  
#  
#Bug Fixes  
#  
# YouTube Stream Now did not work  
# RTMP broadcast could fail to start if server messages were received in the
wrong order  
# RTMP Auto-reconnect did not work  
#  
# Docs:  
#
http://cdn.teradek.com/Public/Sputnik/Docs/Teradek_Sputnik_Setup_Guide_v2_0512.pdf  
FROM debian:jessie  
MAINTAINER Peerasan Buranasanti (Patrickz) <peerasan@gmail.com>  
# Fork from texastribune/sputnik  
LABEL version="1.2"  
FROM debian:jessie  
MAINTAINER Peerasan Buranasanti (Patrickz) <peerasan@gmail.com>  
# Fork from texastribune/sputnik  
LABEL description="Teradek sputnik for Teradek BondII (3G Bonding)"  
ENV DEBIAN_FRONTEND noninteractive  
  
# change repo  
RUN sed -i -e "s/httpredir.debian.org/mirror.kku.ac.th/g"
/etc/apt/sources.list  
  
RUN apt-get update; apt-get upgrade -y;  
RUN apt-get install -y libc6-i386 lib32stdc++6 lib32z1 lib32gcc1  
# http://teradek.com/pages/downloads#sputnik see the link for the 64b .deb  
ADD
http://update.teradek.com/download.php?file=/Teradek/Sputnik/Software/Releases/2.5.x/2.5.2/teradek-
sputnik_2.5.2.r26587_amd64.deb /tmp/teradek-sputnik.deb  
RUN dpkg -i /tmp/teradek-sputnik.deb  
  
# Create volume friendly data directory  
RUN mkdir -p /data/conf  
RUN mv /etc/sputnik*.conf /data/conf/  
RUN ln -s /data/conf/sputnik.conf /etc/ && ln -s /data/conf/sputnik-users.conf
/etc/  
VOLUME ["/data/"]  
  
# WISHLIST how to get sputnik logs into /data ?  
VOLUME ["/var/log/"]  
  
# listening  
EXPOSE 5111  
# web server  
EXPOSE 1957  
# rtsp monitor  
EXPOSE 554  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
CMD ["/start.sh"]  

