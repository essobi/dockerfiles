FROM mbdevpl/usable-ubuntu:latest  
  
MAINTAINER Mateusz Bysiek <mateusz.bysiek.spam@gmail.com>  
  
USER root  
COPY . /root/Projects/docker-usable-python  
WORKDIR /root/Projects/docker-usable-python  
  
#  
#  
#  
RUN bash init_python_packages.sh  
  
#  
#  
#  
  
USER root  
  
RUN cat bash_history.sh >> /root/.bash_history  
  
USER user  
  
RUN cat bash_history_user.sh >> /home/user/.bash_history  
  
WORKDIR /home/user  

