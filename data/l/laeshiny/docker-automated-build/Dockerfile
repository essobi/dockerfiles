# pull image  
FROM ubuntu:14.04  
MAINTAINER Laeshiny version: 0.1  
RUN \  
apt-get update && \  
apt-get install -y apache2 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
VOLUME ["/data1", "/test333"]  
  
EXPOSE 80  
CMD ["ls", "-al"]  

