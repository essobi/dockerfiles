FROM ubuntu  
RUN apt-get update  
RUN apt-get install -y openssh-client curl  
RUN curl -o /usr/bin/websocat -L
https://github.com/vi/websocat/releases/download/v0.4.0/websocat_0.4_x86_64-unknown-
linux-gnu  
RUN chmod +x /usr/bin/websocat  
  
ENV DOCKER_HOST_ADDR 172.17.0.1  
ENV REMOTE_SSH_FWD_PORT 2200  
COPY . .  
CMD ./entrypoint.sh  

