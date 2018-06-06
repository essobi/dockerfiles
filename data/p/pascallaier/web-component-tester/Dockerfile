FROM selenium/standalone-chrome  
  
MAINTAINER Pascal Laier <pascal.laier@abas.de>  
  
RUN sudo apt-get update  
RUN sudo apt-get install -y curl xvfb git  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN sudo apt-get install -y nodejs  
RUN sudo npm install -g bower polymer-cli

