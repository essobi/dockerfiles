FROM ubuntu:16.04  
LABEL maintainer="Brandon Phillips"  
  
# Install wget  
RUN apt-get update && apt-get install -y wget  
  
# Add wvu sources  
RUN wget -r -l1 --no-parent -A "loud-apt*.deb"
http://loud.lcsee.wvu.edu/stable/lxerus  
RUN dpkg -i loud.lcsee.wvu.edu/stable/lxerus/loud-apt*.deb  
RUN apt-get update  
  
# Install the CS450 package  
RUN apt-get install -y loud-cs450-mpx  
  
# Install dependencies  
RUN apt-get install -y gdb valgrind  

