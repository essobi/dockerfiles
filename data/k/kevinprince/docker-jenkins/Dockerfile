# -*- mode: Dockerfile; tab-width: 2 -*-  
FROM jenkins:latest  
USER root  
RUN apt-get update  
RUN apt-get install -y lxc  
RUN rm -rf /var/lib/apt/lists/*  
USER jenkins  

