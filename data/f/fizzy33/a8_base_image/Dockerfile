FROM phusion/baseimage:latest  
  
MAINTAINER Glen Marchesani "https://github.com/fizzy33"  
# make sure we have the latest security patches  
RUN \  
apt-get update && \  
apt-get upgrade -y -o Dpkg::Options::="--force-confold" && \  
apt-get install -y \  
curl \  
fish \  
git \  
httping \  
mtr \  
nano \  
rsync \  
screen \  
unison \  
wget  
  
CMD ["/sbin/my_init"]  
  
  
# == build with ==  
#  
# docker build -t a8_base_image .  

