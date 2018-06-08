#  
# TF2 Dockerfile  
#  
# https://github.com/johnjelinek/tf2server-docker  
#  
# Pull the base image  
FROM ubuntu:14.04  
MAINTAINER John Jelinek IV <john@johnjelinek.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dependencies  
RUN \  
apt-get update && \  
apt-get install -y tmux mailutils postfix lib32gcc1 wget  
  
# Cleanup  
RUN \  
apt-get clean && \  
rm -fr /var/lib/apt/lists/* && \  
rm -fr /tmp/*  
  
# Create user to run as  
RUN groupadd -r tf2server && useradd -rm -g tf2server tf2server  
  
# Install TF2 Server  
RUN wget http://gameservermanagers.com/dl/tf2server && \  
chmod +x tf2server  
  
# Volume  
VOLUME ["/home/tf2server"]  
RUN chown -R tf2server:tf2server /home/tf2server  
  
# Define working directory  
WORKDIR /home/tf2server  
  
USER tf2server  
  
# Default command  
ENTRYPOINT ["./tf2server"]  
  
# Expose port  
# - 27015: Port to serve on  
EXPOSE 27015/tcp  
EXPOSE 27015/udp  

