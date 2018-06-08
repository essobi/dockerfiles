FROM alpine:latest  
Label maintainer="Wolfereign"  
  
# Update Packages and Install Needed Packages  
RUN apk add --update --no-cache \  
samba \  
samba-common-tools \  
supervisor \  
&& rm -rf /var/cache/apk/*  
  
# Copy the supervisord configuration file  
COPY supervisord.conf /etc/supervisord.conf  
  
# Expose Needed ports (137/udp and 138udp for nmbd)(139 and 445 for smbd)  
EXPOSE 137/udp 138/udp 139 445  
# Supervisord will run the samba services in the foreground and redirect logs  
ENTRYPOINT ["supervisord"]  

