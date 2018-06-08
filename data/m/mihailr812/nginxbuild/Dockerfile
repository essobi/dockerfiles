FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y curl python-software-properties
software-properties-common && add-apt-repository ppa:nginx/stable  
RUN echo "deb-src http://ppa.launchpad.net/nginx/development/ubuntu xenial
main" >> /etc/apt/sources.list.d/nginx-ubuntu-development-xenial-list  
RUN apt-get update && apt-get build-dep -y nginx  
RUN cd /opt && apt-get source -y nginx  

