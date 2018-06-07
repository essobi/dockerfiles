FROM ubuntu:16.04 as itksoftwareguide-base  
MAINTAINER Matt McCormick <matt.mccormick@kitware.com>  
  
RUN apt-get update && apt-get install -y \  
apt-utils \  
build-essential \  
ccache \  
curl \  
git \  
ninja-build \  
python \  
vim \  
&& apt-get clean  
  
# Install the latest CMake release  
WORKDIR /tmp/  
#RUN curl -L https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \  
#python get-pip.py && \  
#pip install cmake  
#WORKDIR /  
# Build and install CMake from source for Ninja build job patch to be released
with CMake 3.11  
# Commit 07185055d57f28347a1850a1f06787ac93f20afd  
WORKDIR /usr/src  
RUN apt-get install -y libncurses-dev libssl-dev && \  
git clone https://github.com/Kitware/CMake.git CMake && \  
cd CMake && \  
git checkout e841ae823edc3021aaa5b297be715344a9bca47e && \  
mkdir /usr/src/CMake-build && \  
cd /usr/src/CMake-build && \  
/usr/src/CMake/bootstrap \  
\--parallel=5 \  
\--prefix=/usr && \  
make -j5 && \  
./bin/cmake \  
-DCMAKE_BUILD_TYPE:STRING=Release \  
-DCMAKE_USE_OPENSSL:BOOL=ON . && \  
make install && \  
cd .. && \  
rm -rf CMake* && \  
apt-get clean  
WORKDIR /  
  
# Using --no-install-recommends greatly reduces the installed packages  
RUN apt-get update && apt-get install -y --no-install-recommends \  
texlive-latex-base \  
texlive-latex-extra  
RUN apt-get update && apt-get install -y \  
dvipng \  
ghostscript \  
locales \  
imagemagick \  
python \  
python-pygments \  
latex-xcolor \  
tex4ht \  
texlive-fonts-recommended \  
&& apt-get clean  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \  
locale-gen  
ENV LC_ALL=en_US.UTF-8 \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8  

