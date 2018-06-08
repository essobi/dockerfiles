FROM ubuntu:16.04  
MAINTAINER Maxim Makarov <m@csgo.com>  
  
RUN useradd -m meteor && \  
apt-get update && \  
apt-get install -y curl git-core  
  
USER meteor  
  
RUN curl https://install.meteor.com/ | sh  
ENV PATH /home/meteor/.meteor:$PATH  
  
CMD meteor

