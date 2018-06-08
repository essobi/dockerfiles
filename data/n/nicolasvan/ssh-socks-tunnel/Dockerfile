  
FROM alpine:3.5  
  
RUN apk add \--no-cache openssh; \  
adduser -D user; mkdir /home/user/.ssh; chown user:user /home/user/.ssh; chmod
0700 /home/user/.ssh; \  
touch /home/user/.ssh/authorized_keys; chown user:user
/home/user/.ssh/authorized_keys  
  
ADD entrypoint.sh /entrypoint.sh  
  
EXPOSE 22  
CMD ["sh", "/entrypoint.sh"]  

