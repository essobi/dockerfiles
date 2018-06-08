FROM ubuntu:latest  
  
ENV VERSION 4.0.1  
  
RUN apt update && \  
apt install -y software-properties-common && \  
add-apt-repository -y ppa:oisf/suricata-stable && \  
apt update && \  
apt install -y suricata && \  
apt purge -y software-properties-common && \  
rm -rf /var/lib/apt/lists/  
  
WORKDIR /root  

