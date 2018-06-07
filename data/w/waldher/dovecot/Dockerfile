FROM alpine:3.5  
RUN apk add --no-cache dovecot=2.2.27-r0  
  
VOLUME "/etc/dovecot"  
  
EXPOSE 143  
EXPOSE 993  
ENTRYPOINT ["/usr/sbin/dovecot", "-F"]  

