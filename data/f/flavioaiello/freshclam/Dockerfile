FROM alpine:3.7  
COPY files /  
  
RUN set -ex ;\  
apk update;\  
apk upgrade;\  
apk add --no-cache su-exec tini clamav clamav-libunrar ;\  
rm -rf /var/cache/apk/*;\  
mkdir /run/clamav/;\  
chown clamav:clamav /run/clamav/  
  
ENTRYPOINT ["/sbin/tini", "--", "entrypoint.sh"]  
CMD ["freshclam", "-d", "-c", "6"]  

