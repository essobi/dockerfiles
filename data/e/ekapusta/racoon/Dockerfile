FROM debian:jessie  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y racoon
ipsec-tools  
  
COPY run.sh /run.sh  
RUN chmod a+x /run.sh  
CMD "/run.sh"  

