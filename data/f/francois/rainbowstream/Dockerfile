# Base docker image  
FROM debian:jessie  
MAINTAINER François Billant <fbillant@gmail.com>  
  
RUN sed -i.bak 's/jessie main/jessie main contrib non-free/g'
/etc/apt/sources.list && \  
  
apt-get update && \  
apt-get install -y \  
python-dev python-pip libfreetype6 libfreetype6-dev zlib1g-dev  
  
RUN pip install rainbowstream  
  
CMD ["/usr/local/bin/rainbowstream"]  

