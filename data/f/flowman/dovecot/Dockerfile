FROM alpine:edge  
  
RUN \  
apk add --no-cache \  
dovecot \  
dovecot-mysql \  
dovecot-pigeonhole-plugin \  
&& mkdir -p /data/domains \  
&& chown mail:mail /data  
  
COPY ./dovecot /etc/dovecot  
  
COPY ./gencert.sh ./docker-entrypoint.sh /  
  
RUN chmod +x /docker-entrypoint.sh /gencert.sh  
  
VOLUME ["/data"]  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 143 993 4190  
CMD ["dovecot", "-F"]

