FROM alpine:latest  
  
RUN apk add --no-cache avahi  
RUN sed -i -r 's/^[[:blank:]]*#?[[:blank:]]*enable-
dbus[[:blank:]]*=.*$/enable-dbus=no/' /etc/avahi/avahi-daemon.conf  
  
CMD ["/usr/sbin/avahi-daemon"]  
  
EXPOSE 5353/udp  
  
VOLUME ["/etc/avahi"]  

