FROM registry.fedoraproject.org/fedora:latest  
MAINTAINER Marco Cyriacks <marco@cyriacks.net>  
  
RUN dnf upgrade -y  
RUN dnf install -y texlive-scheme-full  
RUN dnf install -y git doxygen graphviz make  
  
# Set correct timezone  
ENV TZ=Europe/Berlin  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  

