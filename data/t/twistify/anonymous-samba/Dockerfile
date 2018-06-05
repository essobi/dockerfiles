# BUILD: sudo docker build -t anonymous-samba .  
# RUN: sudo docker run -it -d -p 445:445 --name smb anonymous-samba  
# RUN WITH VOLUME: sudo docker run -it -d -p 445:445 -v samba-data:/data
--name smb anonymous-samba  
# LOGIN: smb://your-ip-or-url/ as Guest (no password)  
FROM alpine:3.5  
LABEL maintainer "@twistify"  
LABEL description "Anonymous Samba Server"  
  
RUN apk --no-cache add \  
samba \  
samba-common-tools \  
&& mkdir -p /data/shared \  
&& chmod 777 /data/shared \  
&& chown nobody:nogroup /data/shared  
  
VOLUME ["/data"]  
  
COPY smb.conf /etc/samba/smb.conf  
  
EXPOSE 445  
# Start Samba  
# F: run in foreground  
# S: cause smbd to log to standard output rather than a file  
ENTRYPOINT ["smbd", "-FS"]  

