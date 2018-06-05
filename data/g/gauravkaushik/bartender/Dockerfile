FROM gauravkaushik/ubuntu:latest  
  
MAINTAINER "Gaurav Kaushik" <gaurav@sevenbridges.com>  
  
RUN apt-get update -y && apt-get install wget zlib1g-dev libncurses5-dev vim
gcc git python-dev python-pip build-essential -y  
  
RUN mkdir /usr/bin/bartender_setup && cd /usr/bin/bartender_setup  
  
RUN git init && git pull https://github.com/LaoZZZZZ/bartender-1.1  
  
RUN sudo make install  
  
CMD ["/bin/bash"]

