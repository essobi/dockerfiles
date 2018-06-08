FROM alpine:3.7  
COPY files /  
  
RUN set -ex ;\  
apk update;\  
apk upgrade;\  
apk add --no-cache su-exec tini rspamd ca-certificates;\  
rm -rf /var/cache/apk/*;\  
mkdir /run/rspamd  
  
ENTRYPOINT ["/sbin/tini", "--", "entrypoint.sh"]  
CMD ["rspamd", "-u", "rspamd", "-g", "rspamd", "-f"]  

