ARG FROM_IMAGE=ubuntu:14.04  
FROM ${FROM_IMAGE}  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -yq \  
software-properties-common && \  
add-apt-repository ppa:george-edison55/cmake-3.x && \  
add-apt-repository ppa:git-core/ppa && \  
apt-get update && apt-get install -yq \  
build-essential \  
nano \  
git \  
wget \  
cmake \  
python \  
mariadb-server \  
gdb-multiarch && \  
apt-get -y autoremove && \  
apt-get -y autoclean  
  
ENV HOME=/home/developer  
  
RUN useradd --user-group --create-home --home-dir $HOME developer && \  
chown -R developer:developer $HOME  
  
USER developer

