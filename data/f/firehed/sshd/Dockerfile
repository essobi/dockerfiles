FROM alpine:3.6  
RUN apk add --no-cache openssh-server  
  
WORKDIR /ssh  
COPY sshd_config .  
COPY start.sh .  
  
EXPOSE 22  
CMD sh start.sh  

