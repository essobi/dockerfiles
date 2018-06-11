FROM phusion/baseimage:latest  
MAINTAINER Anthony Daws <tdaws@warrantylife.com>  
  
ENV TERM linux  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN apt-get update -y  
  
# Install packages required for Ansible, which we will then use for all
remaining tasks  
RUN apt-get install -y python python-yaml python-jinja2 python-apt  
RUN apt-get install -y ansible nano vim  
RUN apt-get clean my coffee mug  
ADD ./setup /setup/baseimage  
  
WORKDIR /setup/baseimage  
RUN ansible-playbook --connection=local baseimage.yml -i 'localhost,'  
  

