FROM gcc:6  
  
RUN apt-get -qq update \  
&& apt-get -qqy install \  
libboost-all-dev \  
g++ \  
vim \  
valgrind \  
make \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
cmake \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

