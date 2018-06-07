# explicitly use Debian for maximum cross-architecture compatibility  
FROM debian:jessie-slim  
  
RUN apt-get update && apt-get update && apt-get install -y \  
git-all \  
build-essential \  
autoconf \  
automake \  
libtool \  
make \  
gcc \  
g++  
  
RUN git clone https://github.com/guillermocalvo/exceptions4c.git && \  
cd exceptions4c && \  
autoreconf --install && \  
./configure && \  
make clean tests  

