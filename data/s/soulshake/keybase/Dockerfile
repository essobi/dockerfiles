FROM debian:jessie  
MAINTAINER AJ Bowen <aj@soulshake.net>  
  
RUN apt-get update && apt-get install -y \  
gnupg \  
curl \  
libappindicator1 \  
fuse \  
sudo  
  
RUN groupadd -g 1000 keybase \  
&& useradd --create-home -d /home/keybase -g keybase -u 1000 keybase  
RUN echo "keybase ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
USER keybase  
ENV HOME /home/keybase  
  
WORKDIR /home/keybase  
  
RUN curl -O https://prerelease.keybase.io/keybase_amd64.deb  
RUN sudo dpkg -i keybase_amd64.deb  
RUN sudo apt-get install -f  
RUN run_keybase  
RUN mkdir $HOME/.config  
  
ENTRYPOINT ["keybase"]  

