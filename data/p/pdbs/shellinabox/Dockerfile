FROM ubuntu:latest  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install
shellinabox openssh-client && \  
apt clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY *.css /etc/shellinabox/  
COPY start.sh /  
  
RUN chmod 0750 /start.sh  
  
EXPOSE 4200  
ENTRYPOINT /start.sh  

