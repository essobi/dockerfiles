##########################################  
## Dockerfile ##  
##########################################  
  
FROM ubuntu:14.04  
RUN apt-get update \  
&& apt-get install -y \  
build-essential \  
wget \  
python \  
make \  
gcc \  
unzip \  
libcppunit-dev \  
libcppunit-doc \  
cmake \  
python \  
git \  
zip \  
valgrind \  
tree \  
vim \  
nano \  
libsnappy-dev \  
zlib1g-dev \  
libbz2-dev \  
libgflags-dev \  
tar \  
curl \  
lcov \  
&& rm -rf /var/lib/apt/lists/*  
MAINTAINER gisedaye gisedaye  
COPY ./ /home  
RUN cd /home/AppServer && chmod 777 install.sh && ./install.sh -docker  
WORKDIR /home/AppServer/build  
CMD ["bash"]  
  

