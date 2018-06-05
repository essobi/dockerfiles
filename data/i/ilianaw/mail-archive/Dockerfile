FROM alpine:edge  
RUN apk add --no-cache dovecot && mkdir /mail \  
&& rm -rv /etc/ssl/dovecot/* /etc/dovecot/*  
ADD dovecot.conf start.sh /etc/dovecot/  
VOLUME ["/mail"]  
CMD ["/etc/dovecot/start.sh"]  
EXPOSE 993  

