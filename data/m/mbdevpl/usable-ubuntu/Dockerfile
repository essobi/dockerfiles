FROM ubuntu:18.04  
  
MAINTAINER Mateusz Bysiek <mateusz.bysiek.spam@gmail.com>  
  
SHELL ["/bin/bash", "--login", "-c"]  
  
USER root  
COPY . /root/Projects/docker-usable-ubuntu  
WORKDIR /root/Projects/docker-usable-ubuntu  
  
#  
#  
#  
RUN bash init_ubuntu_base.sh  
  
RUN bash init_ubuntu_base_user.sh  
  
#  
# configure git for local usage  
#  
  
USER user  
WORKDIR /home/user  
  
RUN git config \--global user.email "ubuntu-user@example.com"  
RUN git config \--global user.name "Ubuntu User"  
#  
# initialize bash history  
#  
  
USER root  
WORKDIR /root/Projects/docker-usable-ubuntu  
  
RUN cat bash_history.sh >> /root/.bash_history  
  
USER user  
  
RUN cat bash_history_user.sh >> /home/user/.bash_history  
  
WORKDIR /home/user  
  
ENTRYPOINT ["/bin/bash", "--login"]  

