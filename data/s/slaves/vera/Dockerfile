FROM ubuntu:xenial  
  
ENV DEBIAN_FRONTEND=noninteractive  
ENV PATH=$PATH:/bin/:/usr/bin/  
  
# Apt packages  
ADD apt_requirements.txt apt_requirements.txt  
  
RUN apt-get update  
RUN apt-get install -y $(grep -vE "^\s*#" apt_requirements.txt | tr "\n" " ")  
  
# Download Vera++  
ADD https://bitbucket.org/verateam/vera/downloads/vera++-1.3.0.tar.gz
vera++-1.3.0.tar.gz  
RUN tar zxvf vera++-1.3.0.tar.gz  
  
# build and install  
RUN cd vera++-1.3.0 && mkdir build  
RUN cd vera++-1.3.0/build; cmake ..  
RUN cd vera++-1.3.0/build; make -j8  
RUN cd vera++-1.3.0/build; make install  
  
#cleanup  
RUN rm ./vera++-1.3.0.tar.gz  
RUN apt-get -y autoremove  
RUN apt-get -y autoclean  
RUN apt-get -y purge wget  

