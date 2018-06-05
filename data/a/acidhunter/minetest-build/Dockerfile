############################################################  
# Dockerfile to bulid container images containing the requirements for
minetest  
# Based on Ubuntu  
############################################################  
  
FROM ubuntu:zesty  
MAINTAINER Martin F. acidhunter <npanic@kmpt.nz>  
  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y openssh-client rsync curl git  
  
RUN \  
apt-get update && \  
apt-get install -y postgresql-client-9.6 libpq5 libpq-dev libirrlicht-dev
cmake libbz2-dev libpng-dev libjpeg-dev libxxf86vm-dev libgl1-mesa-dev
libsqlite3-dev libogg-dev libvorbis-dev libopenal-dev libcurl4-gnutls-dev
libfreetype6-dev zlib1g-dev libgmp-dev libjsoncpp-dev  
  
ENV HOME /root  
WORKDIR /root  
CMD ["bash"]  

