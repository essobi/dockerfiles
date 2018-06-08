FROM ubuntu:latest  
  
WORKDIR /source  
  
RUN apt-get update && apt-get install -y \  
g++ \  
cmake \  
git \  
cppcheck \  
qt5-default \  
qtbase5-dev \  
lcov \  
&& rm -rf /var/lib/apt/lists/*  

