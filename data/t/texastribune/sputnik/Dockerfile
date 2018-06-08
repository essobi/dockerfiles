# Teradek Sputnik  
#  
# Docs:  
#
http://cdn.teradek.com/Public/Sputnik/Docs/Teradek_Sputnik_Setup_Guide_v2_0512.pdf  
FROM debian:squeeze  
MAINTAINER tech@texastribune.org  
  
RUN apt-get update -qq  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq libc6-i386 lib32stdc++6
lib32z1  
# http://teradek.com/pages/downloads#sputnik see the link for the 64b .deb  
ADD
http://update.teradek.com/download.php?file=/Teradek/Sputnik/Software/Releases/2.2.x/2.2.1/teradek-
sputnik_2.2.1.r22961_amd64.deb /tmp/teradek-sputnik.deb  
RUN DEBIAN_FRONTEND=noninteractive dpkg -i /tmp/teradek-sputnik.deb  
  
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
CMD ["/start.sh"]  

