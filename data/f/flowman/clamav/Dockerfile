FROM alpine:latest  
  
RUN \  
apk add --no-cache \  
clamav \  
clamav-libunrar \  
&& mkdir /run/clamav  
  
COPY ./clamd.conf ./freshclam.conf /etc/clamav/  
  
COPY ./docker-entrypoint.sh /  
  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 3310  
CMD ["clamd"]

