## start with the latest Ubuntu image  
FROM ubuntu:latest  
  
## Maintainer  
MAINTAINER "Jan Tilly" jantilly@gmail.com  
  
## Set working directory  
WORKDIR /root  
  
## Remain current  
RUN apt-get update -qq \  
&& apt-get dist-upgrade -y  
  
## Add compilers, make, and valgrind  
RUN apt-get update -qq \  
&& apt-get install -y --no-install-recommends \  
g++ \  
gcc \  
gfortran \  
make \  
valgrind  
  
## Add lapack / blas  
RUN apt-get update -qq \  
&& apt-get install -y --no-install-recommends \  
libblas3gf \  
libblas-dev \  
liblapack3gf \  
liblapack-dev  
  
## Install python-dev and python-pip  
RUN apt-get update -qq \  
&& apt-get install -y --no-install-recommends \  
python-dev \  
python-pip  
  
## Install numpy, petsc and pets4py  
RUN pip install numpy \  
&& pip install petsc --allow-external petsc \  
&& pip install petsc4py --allow-external petsc4py  
  
## Install git and clone tao  
RUN apt-get install git -y --no-install-recommends \  
&& cd ~ \  
&& git clone https://github.com/jtilly/taopy  
  
## Clean-up  
RUN rm -rf /tmp/* && rm -rf /var/lib/apt/lists/*  

