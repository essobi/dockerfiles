FROM debian:8  
  
RUN apt update && \  
apt install -y osmctools && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
USER 1000  
WORKDIR /code  

