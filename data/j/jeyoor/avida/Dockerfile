FROM ubuntu:14.04  
MAINTAINER Jeyan Oorjitham <jeyoor@gmx.com>  
RUN apt-get update && apt-get install -y \  
build-essential \  
cmake \  
git \  
libncurses-dev  
RUN git clone https://github.com/devosoft/avida.git  
RUN ["/bin/bash", "-c", "cd avida; ./build_avida"]  
CMD ["/bin/sh", "-c", "cd /avida/cbuild/work; exec /bin/bash"]  

