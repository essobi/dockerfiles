FROM alpine:latest  
LABEL maintainer="Mark Stillwell <mark@stillwell.me>"  
  
RUN apk add --update-cache --no-cache \  
dumb-init \  
syslog-ng \  
ssmtp \  
supervisor && \  
rm -rf \  
/etc/ssmtp/* \  
/etc/syslog-ng/* \  
/var/cache/apk/* \  
/var/log/*  
  
RUN mkdir -m 0755 -p /etc/my_init.d /usr/local/share/my_init  
COPY root/usr/local/share/my_init/functions.sh /usr/local/share/my_init/  
COPY root/usr/local/sbin/my_init.sh /usr/local/sbin/  
RUN chmod 0755 /usr/local/sbin/my_init.sh
/usr/local/share/my_init/functions.sh  
CMD ["/usr/local/sbin/my_init.sh"]  
  
RUN mkdir -m 0755 /etc/supervisor /etc/supervisor/conf.d  
COPY root/etc/supervisord.conf /etc/  
RUN chmod 0644 /etc/supervisord.conf  
  
COPY root/etc/my_init.d/05-ssmtp-setup /etc/my_init.d/  
RUN chmod 0755 /etc/my_init.d/05-ssmtp-setup  
  
COPY root/etc/my_init.d/05-syslog-setup /etc/my_init.d/  
RUN chmod 0755 /etc/my_init.d/05-syslog-setup  

