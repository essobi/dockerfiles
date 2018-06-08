FROM ubuntu:16.04  
MAINTAINER Ovidiu-Florin Bogdan (ovidiu-florin@kubuntu.org)  
  
RUN apt update  
RUN apt install -yy packaging-dev  
  
RUN useradd developer && echo 'developer ALL=(ALL) NOPASSWD:ALL' >>
/etc/sudoers  
  
USER developer  
  
VOLUME /home/developer  
WORKDIR /home/developer  
  
VOLUME /var/cache/pbuilder  
  
COPY setup.py /setup.py  
  
CMD clear && /setup.py && bash  

