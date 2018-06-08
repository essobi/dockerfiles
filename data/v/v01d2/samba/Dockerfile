FROM alpine  
RUN \  
apk -U add samba  
  
ADD smb.conf /etc/samba  
  
RUN \  
rm -rf /var/cache/apk/*  
  
EXPOSE 139 445  
ENTRYPOINT exec /usr/sbin/smbd -FS < /dev/null  

