FROM alpine  
RUN apk --update add sshfs certbot bash; rm -rf /var/cache/apk/*  
COPY bin /usr/local/bin  
RUN chmod +x /usr/local/bin/entrypoint.sh; mkdir -p /etc/letsencrypt  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

