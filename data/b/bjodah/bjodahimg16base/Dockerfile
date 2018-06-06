# DO NOT EDIT, This Dockerfile is generated from
./tools/05_generate_base_Dockerfile.sh  
FROM ubuntu:xenial  
MAINTAINER Björn Dahlgren <bjodah@DELETEMEgmail.com>  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN true  
RUN apt-get update && \  
apt-get \--quiet \--assume-yes install locales && \  
locale-gen en_US.UTF-8 && \  
echo "path-exclude /usr/share/doc/*" >/etc/dpkg/dpkg.cfg.d/01_nodoc && \  
echo "path-include /usr/share/doc/*/copyright" >>/etc/dpkg/dpkg.cfg.d/01_nodoc
&& \  
apt-get upgrade && \  
apt-get \--assume-yes \--no-install-recommends install  wget curl unzip git
build-essential gfortran \  
devscripts cdbs libtool flex bison fakeroot equivs checkinstall lintian \  
binutils-dev dpkg-dev autotools-dev \  
liblapack-dev libicu-dev zlib1g-dev libbz2-dev libyaml-dev \  
libopenmpi-dev libgmp-dev libmpfr-dev libfreetype6-dev libpng12-dev \  
libjpeg-dev libatlas-base-dev libzmq3-dev libxslt1-dev libxml2-dev \  
python-dev python3-dev python-all python-all-dev \  
python3-all python3-all-dev && \  
cd /tmp && \  
for FNAME in get-pip.py; do \  
curl -LOs
"http://hera.physchem.kth.se/~repo/bjodahimg16base/v1.2/blobs/$FNAME"; \  
done && \  
python2 get-pip.py && \  
python3 get-pip.py && \  
rm get-pip.py && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

