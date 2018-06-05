FROM marklee77/supervisor:alpine  
LABEL maintainer="Mark Stillwell <mark@stillwell.me>"  
  
RUN adduser -u 1000 -h /var/bind -s /bin/false -D named && \  
apk add --update-cache --no-cache \  
bind \  
bind-tools \  
dnssec-root && \  
mv /var/bind/pri/localhost.zone /etc/bind/db.localhost && \  
mv /var/bind/pri/127.zone /etc/bind/db.127 && \  
rm -rf \  
/etc/bind/named.conf.* \  
/var/bind/* \  
/var/cache/apk/*  
  
COPY root/etc/bind/*.conf /etc/bind/  
RUN chmod 0644 /etc/bind/*.conf  
  
COPY root/etc/my_init.d/10-bind-setup /etc/my_init.d/  
RUN chmod 0755 /etc/my_init.d/10-bind-setup  
  
COPY root/etc/supervisor/conf.d/bind.conf /etc/supervisor/conf.d/  
RUN chmod 0644 /etc/supervisor/conf.d/bind.conf  
  
EXPOSE 53 53/udp  
  
VOLUME ["/var/bind"]  
  
HEALTHCHECK CMD ["rndc", "status"]  

