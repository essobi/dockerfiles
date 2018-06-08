FROM xataz/alpine:3.3  
MAINTAINER xataz <https://github.com/xataz>  
  
EXPOSE 137 138 139 445  
RUN apk add -U \  
samba \  
samba-common-tools \  
acl \  
bc \  
supervisor  
  
ADD rootfs /  
RUN chmod +x /usr/bin/startup  
  
CMD ["tini","--","/usr/bin/startup"]  

