FROM java:7  
  
RUN apt-get update && \  
apt-get install -y file net-tools ppp module-init-tools expect supervisor  
  
ADD NetExtender.Linux.7.5.773.x86_64.tgz /netextender  
ADD start.sh install_netextender /  
RUN /install_netextender  
  
ENTRYPOINT ["/start.sh"]  
  

