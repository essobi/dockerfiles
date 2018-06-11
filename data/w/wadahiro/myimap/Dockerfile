FROM alpine:3.6  
RUN apk -v --update add \  
dovecot \  
dovecot-pigeonhole-plugin \  
fetchmail \  
&& \  
rm /var/cache/apk/*  
  
# Default password for this imap server  
ENV IMAP_USER=myimap  
ENV IMAP_PASSWORD=password  
  
ENV FETCH_INTERVAL=30  
ENV FETCH_ENABLED=false  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/*.sh  
  
COPY fetchmailrc.tmpl /root/  
  
COPY dovecot.conf /etc/dovecot/  
COPY 10-auth.conf /etc/dovecot/conf.d/  
COPY 10-mail.conf /etc/dovecot/conf.d/  
COPY 10-master.conf /etc/dovecot/conf.d/  
COPY 15-lda.conf /etc/dovecot/conf.d/  
COPY 20-managesieve.conf /etc/dovecot/conf.d/  
COPY 90-plugin.conf /etc/dovecot/conf.d/  
COPY 90-sieve.conf /etc/dovecot/conf.d/  
  
EXPOSE 143  
EXPOSE 993  
EXPOSE 4190  
ENTRYPOINT [ "/usr/local/bin/docker-entrypoint.sh" ]  
  

