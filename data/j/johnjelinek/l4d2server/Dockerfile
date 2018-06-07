#  
# L4D2 Dockerfile  
#  
# https://github.com/johnjelinek/l4d2server-docker  
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
RUN groupadd -r l4d2server && useradd -rm -g l4d2server l4d2server  
  
# Install L4D2 Server  
RUN wget http://gameservermanagers.com/dl/l4d2server && \  
chmod +x l4d2server  
  
# Volume  
VOLUME ["/home/l4d2server"]  
RUN chown -R l4d2server:l4d2server /home/l4d2server  
  
# Define working directory  
WORKDIR /home/l4d2server  
  
USER l4d2server  
  
# Default command  
ENTRYPOINT ["./l4d2server"]  
  
# Expose port  
# - 27015: Port to serve on  
EXPOSE 27015/tcp  
EXPOSE 27015/udp  

