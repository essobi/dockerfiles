# Base docker image  
FROM debian:jessie  
MAINTAINER François Billant <fbillant@gmail.com>  
  
RUN apt-get update && apt-get install -y iptables  
  
COPY run.sh /opt/run.sh  
  
RUN chmod +x /opt/run.sh  
  
CMD ["/opt/run.sh"]  

