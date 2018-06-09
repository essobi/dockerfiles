FROM ubuntu:trusty  
MAINTAINER Bruno Furtado <bmfurtado@geekoo.eu>  
  
RUN apt-get update && \  
apt-get install -qy --force-yes transmission-daemon && \  
mkdir -p /var/lib/transmission-daemon/.config/transmission-daemon && \  
mkdir -p /var/lib/transmission-daemon/incomplete && \  
mkdir -p /var/lib/transimssion-daemon/downloads && \  
chown debian-transmission: /var/lib/transmission-daemon/incomplete
/var/lib/transmission-daemon/downloads && \  
chown debian-transmission: /var/lib/transmission-daemon/.config/transmission-
daemon && \  
usermod -d /var/lib/transmission-daemon debian-transmission  
  
ADD settings.json /etc/transmission-daemon/settings.json  
  
VOLUME ["/var/lib/transmission-daemon"]  
  
USER debian-transmission  
  
EXPOSE 51413 9091  
  
CMD /usr/bin/transmission-daemon -f -g /var/lib/transmission-daemon/info  

