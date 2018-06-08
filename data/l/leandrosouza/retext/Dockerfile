FROM ubuntu:14.04  
MAINTAINER Leandro Souza <leandrocsfrb@gmail.com>  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN apt-get update  
RUN apt-get -f install -q -y python3-pyqt5.qtwebkit python3-pip  
RUN /usr/bin/pip3 install markups markdown docutils pyenchant  
RUN /usr/bin/pip3 install ReText  
  
CMD retext

