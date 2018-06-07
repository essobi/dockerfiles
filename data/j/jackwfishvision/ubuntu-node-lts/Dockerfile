FROM ubuntu:xenial  
MAINTAINER Jack Willis-Craig <jackw@fishvision.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Remove sh  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Install packages  
RUN apt update  
RUN apt -y install wget \  
curl \  
git \  
zip \  
unzip \  
libxml2-dev \  
build-essential \  
software-properties-common \  
libssl-dev \  
python \  
python-dev \  
python-pip \  
python-virtualenv \  
vim \  
jq \  
coreutils \  
openssh-client \  
apt-transport-https \  
libelf1 # Required by flow-bin  
  
RUN curl -o- https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
# Install awscli  
RUN pip install awscli  
  
# Clean apt  
RUN apt clean  
  
# Misc  
RUN mkdir -p ~/.ssh  
RUN [[ -f /.dockerenv ]] && echo -e "Host *\n\tStrictHostKeyChecking no\n\n" >
~/.ssh/config  

