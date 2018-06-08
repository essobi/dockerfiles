# Base docker image  
FROM debian:jessie  
MAINTAINER François Billant <fbillant@gmail.com>  
  
RUN sed -i.bak 's/jessie main/jessie main contrib non-free/g'
/etc/apt/sources.list && \  
  
apt-get update && \  
apt-get install -y \  
mutt  
  
# Autorun jdowloader  
CMD ["/usr/bin/mutt"]  

