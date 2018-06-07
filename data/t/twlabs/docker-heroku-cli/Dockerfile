FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -y wget  
RUN wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh  
RUN wget
https://download.docker.com/linux/ubuntu/dists/xenial/pool/stable/amd64/docker-
ce_17.09.0~ce-0~ubuntu_amd64.deb -O docker-ce.deb  
RUN apt-get install -y \  
iptables \  
libltdl7  
RUN dpkg -i docker-ce.deb  

