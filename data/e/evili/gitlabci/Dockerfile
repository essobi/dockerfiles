FROM ubuntu:xenial  
  
#  
# Create and set working directory  
#  
RUN mkdir -pv /src  
WORKDIR /src  
#  
# Install devel packages  
#  
RUN apt-get update && \  
apt-get install --no-install-recommends -y \  
wget build-essential \  
g++ libboost-all-dev \  
subversion git git-flow cmake \  
clang-tidy splint cppcheck \  
valgrind lcov  
#  
# Install some additional devels  
#  
RUN apt-get install --no-install-recommends -y \  
python-pip python3-pip \  
virtualenv python-virtualenv python3-virtualenv \  
mariadb-client libmysqld-dev python-dev libldap-dev \  
libsasl2-dev libjpeg-dev tightvncserver  
  

