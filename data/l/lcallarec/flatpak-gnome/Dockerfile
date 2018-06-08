# Flatpak-gnome  
#  
# VERSION 0.0.1  
FROM ubuntu:17.04  
RUN apt-get update -y  
  
# Install base dependencies  
## For add-apt-repository binary  
RUN apt-get install -y software-properties-common python-software-properties
build-essential  
  
# Install flatpak  
RUN add-apt-repository ppa:alexlarsson/flatpak -y  
RUN apt-get update -y  
RUN apt install flatpak -y  
  
# Install remote  
RUN flatpak remote-add --if-not-exists gnome
https://sdk.gnome.org/gnome.flatpakrepo  
  
# Clean  
RUN apt-get clean -y && apt-get autoclean -y  
  
CMD ["/bin/bash"]  

