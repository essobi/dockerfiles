FROM debian:jessie  
RUN apt-get -y update && apt-get -y upgrade  
RUN apt-get install -y build-essential  
RUN apt-get install -y libc6-dev  
RUN apt-get install -y libc6-dev-i386  
RUN apt-get install -y wget  
RUN apt-get install -y dpatch  
RUN apt-get install -y fakeroot  
RUN apt-get install -y devscripts  
RUN apt-get install -y dh-make  
RUN apt-get install -y apt-utils  
RUN apt-get install -y quilt  
RUN apt-get clean  
VOLUME /opt/package  
# USER sdc  
WORKDIR /opt/package  
CMD /bin/bash

