FROM ubuntu:14.04  
# SSH  
RUN apt-get update &&\  
apt-get install -y openssh-client  
  
# Curl  
RUN apt-get update &&\  
apt-get install -y curl  
  
# Curl  
RUN apt-get update &&\  
apt-get install -y bc  
  
# Jobs  
COPY ./jobs /root/jobs  
  
# Entrypoint  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

