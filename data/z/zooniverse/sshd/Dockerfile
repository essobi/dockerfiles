FROM alpine  
  
RUN apk --no-cache add openssh  
  
RUN adduser -D -u 1001 docker  
RUN passwd -u docker  
  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
COPY sshd_config /etc/ssh/sshd_config  
  
CMD ["/usr/local/bin/entrypoint.sh"]  

