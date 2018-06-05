  
#  
# ubuntu 18.04 dressed up for scientific computing  
#  
FROM ubuntu:18.04  
#  
ENV DEBIAN_FRONTEND=noninteractive  
#  
RUN apt update; apt -yq upgrade; \  
apt install -yq \  
autoconf \  
ca-certificates \  
cmake \  
g++ \  
gawk \  
gfortran-7 \  
git \  
gnuplot \  
libblacs-mpi-dev \  
libblacs-openmpi1 \  
libfftw3-3 \  
libfftw3-bin \  
libfftw3-dev \  
libfftw3-doc \  
libfftw3-double3 \  
libgfortran-7-dev \  
libmatheval1 \  
libmatheval-dev \  
libopenblas-base \  
libopenblas-dev \  
libopenmpi-dev \  
libxext-dev \  
make \  
net-tools \  
openmpi-bin \  
openmpi-common \  
openmpi-doc \  
openssh-server \  
python \  
python3-numpy \  
python3-numpydoc \  
python3-scipy \  
sudo \  
vim \  
wget \  
xxdiff \  
zlib1g zlib1g-dev \  
\--no-install-recommends \  
&& apt autoremove -y \  
&& rm -rf /var/apt/lists/* \  
&& ssh-keygen -A  
#  
RUN \  
ln -s /usr/bin/gfortran-7 /usr/bin/f95 \  
&& ln -s /usr/bin/gfortran-7 /usr/bin/gfortran \  
&& ln -s /usr/bin/gfortran-7 /usr/bin/f90  
  
#  
CMD /bin/bash  
  
  
  
  

