# Base image  
FROM alpine:3.3  
RUN apk add --no-cache openssh rsync  
  
COPY sshd_config /etc/ssh/sshd_config  
ADD entrypoint.sh .  
  
RUN mkdir .ssh  
  
EXPOSE 22  
CMD ["sh", "entrypoint.sh"]

