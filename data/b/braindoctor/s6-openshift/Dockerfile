FROM alpine:latest  
  
RUN \  
apk update && \  
apk upgrade --no-cache && \  
apk add --no-cache s6 && \  
mkdir -p /etc/services.d/.s6-svscan && \  
echo "#!/bin/sh" >> /entrypoint.sh && \  
echo "exec /bin/s6-svscan /etc/services.d" >> /entrypoint.sh && \  
echo "#!/bin/sh" >> /etc/services.d/.s6-svscan/finish && \  
echo "echo \"[s6]: Stopping services...\"" >>
/etc/services.d/.s6-svscan/finish && \  
chmod +x /entrypoint.sh /etc/services.d/.s6-svscan/finish && \  
chmod 777 /etc/services.d && \  
rm -r /var/cache/apk/*  
  
# Register future build instructions  
ONBUILD COPY s6 /etc/services.d  
ONBUILD RUN chmod -R 777 /etc/services.d  
  
ENTRYPOINT ["/entrypoint.sh"]  

