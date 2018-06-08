# Big thanks to @simonbiggs.  
FROM jupyter/jupyterhub:latest  
  
MAINTAINER Spencer Lyon <spencerlyon2@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get -y upgrade  
  
RUN apt-get -y install \  
vim wget  
  
RUN pip install terminado --upgrade && \  
pip3 install terminado --upgrade  
  
  
# Add default user  
RUN useradd -d /home/admin -m admin; \  
echo "admin:admin" | chpasswd; \  
adduser admin sudo  
  
# Start jupyterhub on boot  
CMD jupyterhub -f /srv/jupyterhub/jupyterhub_config.py  

