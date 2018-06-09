FROM ubuntu:16.04  
RUN apt-get update; apt-get -y install thunderbird  
ADD entrypoint.sh /tmp  
  
ENTRYPOINT ["/tmp/entrypoint.sh"]  

