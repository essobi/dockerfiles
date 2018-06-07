FROM alpine:3.7  
RUN set -ex ;\  
apk update;\  
apk upgrade;\  
apk add --no-cache tini su-exec dovecot dovecot-mysql dovecot-pigeonhole-
plugin dovecot-pigeonhole-plugin-extdata rspamd-client;\  
rm -rf /var/cache/apk/*  
  
COPY files /  
  
ENTRYPOINT ["/sbin/tini", "--", "entrypoint.sh"]  
CMD ["/usr/sbin/dovecot", "-c", "/etc/dovecot/dovecot.conf", "-F"]  

