FROM ubuntu:latest  
RUN apt-get update && \  
apt-get install megatools -y  
RUN apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/*  
  
ENV LANG=en_US.UTF-8  

