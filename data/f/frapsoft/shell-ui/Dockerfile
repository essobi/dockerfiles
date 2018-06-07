FROM debian:jessie-slim  
  
MAINTAINER Maik Ellerbrock (https://github.com/ellerbrock)  
  
RUN apt-get update && \  
apt-get install -y whiptail dialog && \  
rm -rf /var/lib/apt/lists/*  
  
COPY ./dotfiles /root  
  
ENTRYPOINT [ "bash" ]  

