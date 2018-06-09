FROM ubuntu  
MAINTAINER Yassine Benhajali <yanamarji@gmail.com>  
RUN apt-get update  
RUN apt-get dist-upgrade -y  
  
RUN sudo apt-get install -y \  
build-essential \  
g++ \  
cmake \  
cmake-curses-gui \  
bison \  
flex \  
freeglut3 \  
freeglut3-dev \  
libxi6 \  
libxi-dev \  
libxmu6 \  
libxmu-dev \  
libxmu-headers \  
bc \  
git  
  
RUN git clone \--recursive git://github.com/BIC-MNI/minc-toolkit.git
/tmp/minc-toolkit  
WORKDIR /tmp/minc-toolkit  
RUN git checkout develop  
RUN git submodule foreach --recursive 'git checkout develop || :'  
RUN mkdir /tmp/minc-build  
WORKDIR /tmp/minc-build  
RUN cmake ../minc-toolkit -DCMAKE_BUILD_TYPE=Release
-DMT_BUILD_VISUAL_TOOLS=ON  
RUN make  
RUN make test  
RUN make install  

