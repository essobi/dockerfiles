FROM ubuntu:wily  
  
RUN apt-get update &&\  
apt-get upgrade -y &&\  
apt-get install -y varnish &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/var/config"]  
  
EXPOSE 80  
ADD start /start  
RUN chmod +x /start  
  
ENTRYPOINT ["/start"]  

