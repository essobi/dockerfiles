FROM rocker/tidyverse:latest  
MAINTAINER Jaehyeon Kim <dottami@gmail.com>  
  
ARG PYTHON_VERSION  
ENV PYTHON_VERSION=${PYTHON_VERSION:-3.6.4}  
  
## https://unix.stackexchange.com/questions/332641/how-to-install-python-3-6  
RUN apt-get update \  
&& apt-get install -y \  
make \  
build-essential \  
libssl-dev \  
zlib1g-dev \  
libbz2-dev \  
libreadline-dev \  
libsqlite3-dev \  
wget \  
curl \  
llvm \  
libncurses5-dev \  
libncursesw5-dev \  
xz-utils \  
tk-dev  
  
## https://stackoverflow.com/questions/41422826/install-python-of-specific-
version-system-wide-with-pyenv/43321411  
RUN git clone https://github.com/pyenv/pyenv.git /root/.pyenv \  
&& /root/.pyenv/plugins/python-build/bin/python-build $PYTHON_VERSION
/usr/local/python-$PYTHON_VERSION/  
  
  
  

