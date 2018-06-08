FROM alpine:3.7  
MAINTAINER David Personette <dperson@gmail.com>  
  
# Install samba  
RUN apk --no-cache --no-progress add bash samba shadow && \  
adduser -D -G users -H -S -g 'Samba User' -h /tmp smbuser && \  
rm -f /etc/samba/smb.conf && \  
rm -rf /tmp/*  
  
COPY smb.conf /etc/samba/  
COPY samba.sh samba-reader.sh /usr/bin/  
  
EXPOSE 137/udp 138/udp 139 445  
HEALTHCHECK \--interval=60s --timeout=15s \  
CMD smbclient -L '\\\localhost\' -U 'guest%' -m SMB3  
  
CMD ["/usr/bin/samba-reader.sh"]  

