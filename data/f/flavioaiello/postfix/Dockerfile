FROM alpine:3.7  
RUN set -ex ;\  
apk update;\  
apk upgrade;\  
apk add --no-cache su-exec tini postfix postfix-mysql ;\  
rm -rf /var/cache/apk/*  
  
COPY files /  
  
ENTRYPOINT ["/sbin/tini", "--", "entrypoint.sh"]  
CMD ["/usr/lib/postfix/master", "-c", "/etc/postfix", "-d"]  

