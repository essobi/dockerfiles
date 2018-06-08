FROM ubuntu:17.04  
  
# Upgrade & install packages  
RUN apt-get update -y \  
&& apt-get upgrade -y \  
&& apt-get install -y p7zip-full curl wget vim git \  
cmake cmake-curses-gui make ninja-build \  
g++ gdb clang ccache doxygen graphviz \  
libboost-all-dev libprotobuf-dev protobuf-compiler \  
&& apt-get clean  
  
RUN mkdir /src  
  
WORKDIR /src  
  
ENV HOME=/tmp  
  
ENTRYPOINT ["/bin/bash"]  

