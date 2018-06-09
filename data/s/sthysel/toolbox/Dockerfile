FROM ubuntu:latest  
MAINTAINER sthysel <sthysel@gmail.com>  
ENV REFRESHED_AT 2015-07-10  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y --no-install-recommends \  
sudo \  
apt-transport-https \  
build-essential \  
cmake \  
git \  
tree \  
vim \  
wireshark \  
ssh \  
silversearcher-ag  
  
RUN apt-get clean && rm -rf /tmp/* /var/tmp/*  
  
# home env  
RUN useradd -ms /bin/bash dev && echo "dev:dev" | chpasswd && adduser dev sudo  
  
ENV HOME /home/dev  
RUN mkdir -p ${HOME} ${HOME}/bin ${HOME}/include  
  
WORKDIR /home/dev  
USER dev  
CMD /bin/bash  

