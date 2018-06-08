FROM alpine:latest  
MAINTAINER Seramo <hello@seramo.com>  
  
RUN apk update && apk upgrade && apk add --no-cache openssh openssh-sftp-
server bash shadow  
RUN rm -rf /var/cache/apk/*  
  
RUN groupadd sftponly  
  
RUN mkdir -p /etc/ssh/keys  
  
COPY sshd_config /etc/ssh/sshd_config  
COPY entrypoint /entrypoint  
  
RUN chmod +x /entrypoint  
  
VOLUME /etc/ssh/keys  
VOLUME /sftp  
  
EXPOSE 22  
CMD /entrypoint  

