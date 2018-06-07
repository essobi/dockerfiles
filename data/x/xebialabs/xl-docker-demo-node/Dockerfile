FROM node:8.5-alpine  
RUN apk add --no-cache openssh supervisor  
ADD resources/supervisord.conf /etc/supervisord.conf  
ADD resources/sshd_config /etc/ssh/sshd_config  
RUN ssh-keygen -A && echo "root:xebialabs" | chpasswd  
  
CMD ["/usr/bin/supervisord"]  
EXPOSE 22 8080

