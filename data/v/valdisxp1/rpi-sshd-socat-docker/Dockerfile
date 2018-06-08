FROM schmich/armv7hf-alpine-qemu:3.5  
MAINTAINER Valdis Adamsons <valdisxp1@gmail.com>  
  
RUN ["cross-build-start"]  
  
RUN apk add --no-cache openssh socat openssl docker  
  
RUN >/etc/motd  
  
RUN ["cross-build-end"]  
  
COPY init.sh update_keys.sh /  
  
COPY sshd_config /etc/ssh/  
  
EXPOSE 22  
CMD [ "/init.sh" ]  

