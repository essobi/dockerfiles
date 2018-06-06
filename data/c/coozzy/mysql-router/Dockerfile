FROM ubuntu:latest  
  
MAINTAINER Marco Egger <m.egger@coozzy.com>  
  
# Arguments  
ENV CLUSTER_URL=localhost CLUSTER_PORT=3306 CLUSTER_USER=cluster
ROUTER_RW_PORT=6446  
  
# Install lsb_release  
RUN apt-get update && apt-get install -y lsb-release wget tzdata  
  
# Install MySQL apt config  
COPY ./mysql-apt-config_0.8.9-1_all.deb /mysql-apt-config.deb  
RUN dpkg -i /mysql-apt-config.deb  
  
# Install MySQL router  
RUN apt-get update \  
&& apt-get install -y mysql-router  
  
# Copy start script  
COPY ./start.sh /start.sh  
  
CMD /start.sh  

