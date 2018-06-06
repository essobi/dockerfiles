# Installs IPython from a fixed commit point on the master branch on GitHub  
# Another Docker container should build from this one to get services like the
notebook  
# docker build -t ptimof/ipython .  
FROM ubuntu:14.04  
MAINTAINER Peter Timofejew <peter@timofejew.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Not essential, but wise to set the lang  
# Note: Users with other languages should set this in their derivative image  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN apt-get update \  
&& apt-get install -y -q language-pack-en \  
&& locale-gen en_US.UTF-8 \  
&& dpkg-reconfigure locales \  
&& apt-get autoremove -y \  
&& apt-get clean -y  
  
# Python binary dependencies, developer tools  
RUN apt-get update \  
&& apt-get install -y -q \  
build-essential \  
curl \  
make \  
gcc \  
zlib1g-dev \  
git \  
python \  
python-dev \  
python-pip \  
python3-dev \  
python3-pip \  
python-sphinx \  
python3-sphinx \  
libzmq3-dev \  
sqlite3 \  
libsqlite3-dev \  
pandoc \  
libcurl4-openssl-dev \  
nodejs \  
nodejs-legacy \  
npm \  
&& apt-get autoremove -y \  
&& apt-get clean -y  
  
# In order to build from source, need less  
RUN npm install -g 'less@<3.0'  
  
RUN pip install invoke  
  
RUN mkdir -p /srv/  
WORKDIR /srv/  
  
# Set commit number (Jan 1, 2015)  
ENV IPYTHON_COMMIT 4694a6690adfc9981514b748bceed6175334aa4e  
  
RUN git clone \--recursive https://github.com/ipython/ipython.git  
WORKDIR /srv/ipython/  
RUN git checkout $IPYTHON_COMMIT  
RUN chmod -R +rX /srv/ipython  
  
# .[all] only works with -e, so use file://path#egg  
# Can't use -e because ipython2 and ipython3 will clobber each other  
RUN pip2 install file:///srv/ipython#egg=ipython[all]  
RUN pip3 install file:///srv/ipython#egg=ipython[all]  
  
# install kernels  
RUN python2 -m IPython kernelspec install-self  
RUN python3 -m IPython kernelspec install-self  
  
WORKDIR /tmp/  
  
RUN iptest2  
RUN iptest3  

