FROM ubuntu:14.04  
MAINTAINER German Schnyder <gschnyder@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV SHELL /bin/bash  
  
RUN apt-get update  
RUN apt-get install -y libx11-6 libXft2 lib32z1 wget bc curl  
RUN mkdir -p /usr/local/workingdir  
  
WORKDIR /usr/local/workingdir  
  
RUN wget http://ssb.stsci.edu/ureka/dev/Ureka_linux-rhe6_64_dev.tar.gz  
  
RUN tar zxf Ureka_linux-rhe6_64_dev.tar.gz  
  
RUN rm -rf Ureka_linux-rhe6_64_dev.tar.gz  
  
RUN Ureka/bin/ur_normalize -s  
  
WORKDIR /root  
  
RUN ["/bin/bash", "-c", "echo \"ur_setup common primary\" >> .profile"]  
  
RUN ["/bin/bash", "-c", "source .profile"]  

