FROM debian:jessie  
  
RUN apt-get update && apt-get install -y fio && \  
mkdir /root/examples && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD examples/ /root/examples  
  
ENTRYPOINT ["fio"]  

