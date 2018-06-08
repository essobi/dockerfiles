FROM alpine:3.5  
MAINTAINER Valdis Adamsons <valdisxp1@gmail.com>  
  
RUN apk add --no-cache openssh socat openssl docker  
  
RUN >/etc/motd  
COPY init.sh update_keys.sh /  
  
COPY sshd_config /etc/ssh/  
  
EXPOSE 22  
CMD [ "/init.sh" ]  

