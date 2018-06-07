# Pull base image  
FROM debian:jessie  
  
  
RUN echo "deb http://ftp.pl.debian.org/debian jessie main" >
/etc/apt/sources.list  
  
# Update packages  
RUN apt-get clean -y && \  
apt-get autoclean -y && \  
apt-get autoremove -y && \  
apt-get update && apt-get install -y git && \  
git clone https://github.com/wolf3d/debian-scripts.git && \  
cd debian-scripts && \  
chmod +x ./bootstrap-opencv && ./bootstrap-opencv  
  
#vim:ts=4  

