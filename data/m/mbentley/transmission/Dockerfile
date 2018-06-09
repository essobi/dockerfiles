FROM alpine:latest  
MAINTAINER Matt Bentley <mbentley@mbentley.net>  
  
RUN (apk --no-cache add transmission-daemon tzdata &&\  
deluser transmission &&\  
addgroup -g 502 transmission &&\  
adduser -h /var/lib/transmission -D -u 502 -g transmission -G transmission -s
/sbin/nologin transmission &&\  
mkdir -p /var/lib/transmission/.config/transmission-daemon &&\  
chown -R transmission:transmission /var/lib/transmission &&\  
ln -sf /usr/share/zoneinfo/US/Eastern /etc/localtime)  
  
COPY settings.json /var/lib/transmission/.config/transmission-
daemon/settings.json  
  
RUN (chown transmission:transmission
/var/lib/transmission/.config/transmission-daemon/settings.json &&\  
chmod 600 /var/lib/transmission/.config/transmission-daemon/settings.json)  
  
USER transmission  
WORKDIR /var/lib/transmission  
EXPOSE 9091 51413/tcp 51413/udp  
VOLUME ["/var/lib/transmission"]  
  
CMD ["/usr/bin/transmission-daemon","-f","--log-error","--log-info"]  

