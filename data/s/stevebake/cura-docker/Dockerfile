FROM ubuntu:xenial  
  
RUN apt-get -y update && \  
apt-get -y install software-properties-common && \  
add-apt-repository ppa:thopiekar/cura && \  
apt-get -y update && \  
apt-get -y install cura  
  
CMD /usr/bin/cura  

