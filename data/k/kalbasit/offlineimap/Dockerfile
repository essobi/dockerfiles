FROM alpine  
  
RUN apk add --update-cache ca-certificates offlineimap \  
&& rm -rf /var/cache/apk/*  
  
VOLUME /var/lib/offlineimap  
VOLUME /etc/offlineimap  
  
CMD ["offlineimap", "-c", "/etc/offlineimap/offlineimaprc", "-u", "basic"]  

