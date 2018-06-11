FROM ubuntu:zesty  
RUN mkdir /root/.ncbi/  
ADD user-settings.mkfg /root/.ncbi/  
RUN apt-get update && \  
apt-get install -y sra-toolkit && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

