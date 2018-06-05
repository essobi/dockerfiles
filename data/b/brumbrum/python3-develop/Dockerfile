ARG DOCKER_TAG  
FROM brumbrum/python3-chrome:$DOCKER_TAG  
MAINTAINER Alessandro Lattao <alessandro.lattao@brumbrum.it>  
  
RUN \  
apt-get \--no-install-recommends -y install gcc python3-pip python3-dev ssh &&
\  
pip3 install virtualenv setuptools wheel && \  
apt-get -y autoclean && \  
apt-get -y clean && \  
apt-get -y autoremove  

