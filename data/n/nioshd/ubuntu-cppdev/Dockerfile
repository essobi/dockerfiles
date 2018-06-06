FROM ubuntu:16.04  
  
LABEL maintainer Mario Werner <mario.werner@iaik.tugraz.at>  
  
# Install commonly used packages for c++ development. Additionally,  
# update-alternatives is configured to simplify use of alternative tools. For  
# example, using gold as default linker  
# `update-alternatives --set ld /usr/bin/ld.gold`.  
#  
# When ccache should be used, the path has to be extended as follows:  
# `export PATH="/usr/lib/ccache:$PATH"`. Note that the default cache directory  
# of ccache can be configured by exporting `CCACHE_DIR`.  
RUN apt-get update && apt-get install -y \  
build-essential \  
ccache \  
clang \  
clang-format \  
clang-tidy \  
cmake \  
curl \  
doxygen \  
git \  
graphviz \  
lcov \  
libboost-all-dev \  
libsqlite3-dev \  
libssl-dev \  
ninja-build \  
python \  
python-pip \  
python3 \  
python3-pip \  
valgrind \  
wget \  
&& pip install --upgrade conan conan_package_tools \  
&& update-alternatives --install "/usr/bin/ld" "ld" "/usr/bin/ld.gold" 10 \  
&& update-alternatives --install "/usr/bin/ld" "ld" "/usr/bin/ld.bfd" 20  
# install docker to permit building images inside of the container  
# https://docs.gitlab.com/ce/ci/docker/using_docker_build.html#using-docker-
build  
RUN curl -sSL https://get.docker.com/ | sh  

