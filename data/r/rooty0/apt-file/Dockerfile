FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y \  
apt-file  
RUN apt-file update  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

