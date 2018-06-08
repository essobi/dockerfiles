FROM phusion/baseimage  
  
RUN adduser --disabled-password --gecos '' docker && \  
adduser docker sudo && \  
echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
USER docker  
  
RUN mkdir /home/docker/workspace && \  
sudo apt-get update && \  
sudo apt-get -y install build-essential software-properties-common curl git-
core man unzip wget  
  
ENV HOME /home/docker  
  
WORKDIR /home/docker/workspace  
  
CMD ["/bin/bash"]  

