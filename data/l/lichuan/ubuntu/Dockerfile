FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y \  
bash-completion \  
curl \  
emacs \  
git \  
screen \  
wget \  
pkg-config  
RUN mkdir -p /root/bin  
COPY bash.bashrc /etc/bash.bashrc  
RUN sed -i '$aexport LC_ALL=C.UTF-8' /root/.bashrc  
RUN sed -i '$aexport PATH=$PATH:/root/bin' /root/.bashrc  
RUN git config --global user.name lichuan  
RUN git config --global user.email 308831759@qq.com  

