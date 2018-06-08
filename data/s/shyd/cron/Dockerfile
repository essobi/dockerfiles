FROM debian:latest  
  
RUN apt-get update && \  
apt-get -y install wget curl rsync openssh-client zip mysql-client cron  
  
RUN rm -rf /var/lib/apt/lists/*  
  
ADD startup.sh /startup.sh  
RUN chmod +x /startup.sh  
  
RUN mkdir /data  
  
WORKDIR /data  
  
CMD /startup.sh  

