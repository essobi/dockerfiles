# YouEarnedIt Ops ops@youearnedit.com  
# Base Dockerfile  
FROM ubuntu:xenial  
  
# Upgrade and install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
apt-transport-https \  
build-essential \  
ca-certificates \  
curl \  
git \  
language-pack-en \  
locales \  
psmisc \  
python-pip \  
python-setuptools \  
software-properties-common \  
sudo \  
&& rm -rf /var/lib/apt/lists/*  
  
# Setup the docker user  
RUN addgroup --gid 9999 docker \  
&& adduser --uid 9999 --gid 9999 --disabled-password --gecos "Docker User"
docker \  
&& usermod -L docker  
  
# Setup the locale options  
RUN locale-gen en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
RUN dpkg-reconfigure locales  
  
# Update pip and setuptools  
RUN pip install --upgrade pip setuptools  
  
# Install the awscli  
RUN pip install awscli  
  
# Become the docker user  
USER docker  

