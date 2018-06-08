FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -y software-properties-common  
RUN DEBIAN_FRONTEND=noninteractive add-apt-repository ppa:ubuntu-lxc/lxd-
stable  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
python \  
python3 \  
python-dev\  
python3-dev\  
golang \  
libssl-dev \  
curl \  
git  
  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get update && apt-get install -y \  
nodejs

