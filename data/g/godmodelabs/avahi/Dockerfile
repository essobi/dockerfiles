FROM debian:latest  
  
RUN apt-get update && apt-get install -y avahi-daemon avahi-utils  
  
RUN sed -i -e "s@#enable-dbus=yes@enable-dbus=no@" /etc/avahi/avahi-
daemon.conf  
  
# Should be started with --net=host  
EXPOSE 5353  
ENTRYPOINT [ "/usr/sbin/avahi-daemon" ]  

