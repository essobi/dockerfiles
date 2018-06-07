FROM debian  
  
RUN apt-get update && \  
apt-get install -y ssh && \  
rm -rf /var/lib/apt/lists/*  
  
COPY ssh/config /root/.ssh/config  
  
COPY deploy /usr/bin  

