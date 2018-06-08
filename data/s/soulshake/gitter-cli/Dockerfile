FROM debian:jessie  
MAINTAINER AJ Bowen <aj@soulshake.net>  
  
RUN apt-get upgrade -y  
RUN apt-get update  
  
RUN apt-get install -y \  
curl \  
sudo  
  
ENV HOME /home/user  
RUN useradd --create-home --home-dir $HOME user \  
&& mkdir -p $HOME/.config/gandi \  
&& chown -R user:user $HOME  
  
RUN echo "user ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
WORKDIR $HOME  
USER user  
RUN echo "alias ll='ls -alhF'" >> $HOME/.bashrc  
  
RUN curl -sL https://deb.nodesource.com/setup_5.x > setup  
RUN sudo -E bash setup  
RUN sudo apt-get install -y nodejs  
RUN sudo npm install -g gitter-cli  
  
ADD ./entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT /entrypoint.sh  

