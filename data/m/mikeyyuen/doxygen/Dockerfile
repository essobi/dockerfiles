FROM ubuntu:16.04  
RUN apt-get update -yqq && \  
apt-get install -yqq \  
bison \  
cmake \  
curl \  
flex \  
g++ \  
git \  
graphviz \  
make \  
python \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN git clone https://github.com/doxygen/doxygen.git /doxygen-build && \  
cd /doxygen-build && \  
mkdir -p build && \  
cd build && \  
cmake -G "Unix Makefiles" .. && \  
make install && \  
rm -rf /doxygen-build  
  
RUN mkdir -p /doxygen && \  
mkdir -p /doxygen/docs && \  
mkdir -p /doxygen/src  
  
COPY doxyfile /doxygen/doxyfile  
  
WORKDIR /doxygen  
  
CMD [ "doxygen" ]  
  

