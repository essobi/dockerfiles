FROM ubuntu:14.04  
RUN apt-get -qq update  
  
# Install useful packages.  
# git : Used by Vundle to get and update plugins.  
# curl : Used by Vundle for searching plugins.  
RUN apt-get -qqy install \  
vim \  
git \  
curl  
  
ENV HOME /home  
  
# Add the .vimrc and other configuration files to the container.  
ADD ./VimConfig $HOME  
  
RUN apt-get -qqy autoremove  
RUN apt-get -qqy clean  
  
ENTRYPOINT /bin/bash  

