#  
# CSGO Dockerfile  
#  
# https://github.com/johnjelinek/csgo-dockerfile  
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
RUN \  
groupadd -r csgoserver && \  
useradd -rm -g csgoserver csgoserver && \  
echo "csgoserver ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
# Install CSGO Server  
RUN wget http://gameservermanagers.com/dl/csgoserver && \  
chmod +x csgoserver  
  
# Volume  
RUN chown -R csgoserver:csgoserver /home/csgoserver  
VOLUME ["/home/csgoserver"]  
  
# Define working directory  
WORKDIR /home/csgoserver  
  
USER csgoserver  
  
# Default command  
ENTRYPOINT ["./csgoserver"]  
  
# Expose port  
# - 27015: Port to serve on  
EXPOSE 27015/tcp  
EXPOSE 27015/udp  

