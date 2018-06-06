FROM marklee77/supervisor:alpine  
LABEL mainteiner="Mark Stillwell <mark@stillwell.me>"  
  
RUN apk add --update --no-cache \  
clamav \  
clamav-libunrar \  
freshclam && \  
rm -rf \  
/etc/periodic/daily/logrotate \  
/var/cache/apk/*  
  
COPY root/etc/clamav/*.conf /etc/clamav/  
RUN chown clamav:clamav /etc/clamav/*.conf && \  
chmod 0644 /etc/clamav/*.conf  
  
COPY root/etc/my_init.d/10-clamav-setup /etc/my_init.d/  
RUN chmod 0755 /etc/my_init.d/10-clamav-setup  
  
COPY root/etc/supervisor/conf.d/clamav.conf /etc/supervisor/conf.d/  
RUN chmod 0644 /etc/supervisor/conf.d/clamav.conf  
  
VOLUME ["/var/lib/clamav"]  
  
EXPOSE 1025  

