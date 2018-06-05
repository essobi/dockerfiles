FROM ubuntu:latest  
MAINTAINER Anthony Nowell <anowell@gmail.com>  
  
ADD https://opscode-omnibus-
packages.s3.amazonaws.com/ubuntu/12.04/x86_64/chefdk_0.2.1-1_amd64.deb /opt/  
RUN dpkg -i /opt/chefdk_0.2.1-1_amd64.deb && rm /opt/chefdk_0.2.1-1_amd64.deb  
  
RUN chef exec gem install knife-acl  
  
WORKDIR /data  
CMD ["knife", "help"]  

