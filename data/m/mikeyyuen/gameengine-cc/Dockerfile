FROM ubuntu:14.04  
MAINTAINER Michael Yuen <michael.yuen@mac.com>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update -yqq && apt-get install -yqq \  
ca-certificates \  
clang-3.6 \  
clang-format-3.6 \  
curl \  
gcc \  
git-core \  
libssl-dev \  
make \  
python \  
time \  
unzip \  
valgrind \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN update-alternatives --install /usr/bin/cc cc /usr/bin/clang-3.6 100 && \  
update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++-3.6 100  
  
ENV DOCKER_VER="17.05.0-ce"  
RUN curl -fsSL -o /tmp/docker-${DOCKER_VER}.tgz
https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VER}.tgz && \  
tar --strip-components=1 -xvzf /tmp/docker-${DOCKER_VER}.tgz -C /usr/local/bin
&& \  
rm /tmp/docker-${DOCKER_VER}.tgz  
  
RUN mkdir -p /gameengine && \  
mkdir -p /gameengine/bin && \  
mkdir -p /gameengine/data && \  
mkdir -p /gameengine/build  
  
ENV PATH "$PATH:/gameengine/bin"  
WORKDIR /gameengine/build  
  

