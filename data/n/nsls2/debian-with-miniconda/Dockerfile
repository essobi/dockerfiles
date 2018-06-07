FROM debian:7.9  
  
MAINTAINER Eric Dill <edill@bnl.gov>  
  
RUN apt-get update && \  
apt-get install -y \  
autoconf \  
build-essential \  
bzip2 \  
gcc \  
g++ \  
git \  
make \  
patch \  
tar \  
wget \  
zlib1g-dev \  
sed \  
libreadline6-dev \  
libglib2.0-0 \  
libxext6 libxext-dev \  
libxrender1 libxrender-dev \  
libsm6 libsm-dev \  
libsmbclient-dev \  
tk-dev \  
libx11-6 libx11-dev \  
# gobject-introspection  
flex \  
# install extra packages for gobject-introspection package  
libffi-dev \  
libssl-dev \  
bison \  
# install packages for hkl  
gtk-doc-tools \  
# need an editor...  
vim \  
# and one for tom...  
emacs  
  
# Set the Locale so conda doesn't freak out  
# It is roughly this problem:
http://stackoverflow.com/questions/14547631/python-locale-error-unsupported-
locale-setting  
# I don't remember exactly where I found this solution, but it took about 2
days of  
# intense googling and trial-and-error  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qq && \  
apt-get install -y locales -qq && \  
locale-gen en_US.UTF-8 en_us && \  
dpkg-reconfigure locales && \  
dpkg-reconfigure locales && \  
locale-gen C.UTF-8 && \  
/usr/sbin/update-locale LANG=C.UTF-8  
ENV LANG C.UTF-8  
ENV LANGUAGE C.UTF-8  
ENV LC_ALL C.UTF-8  
# Add the conda binary folder to the path  
ENV PATH /conda/bin:$PATH  
  
# Actually install miniconda  
RUN cd && \  
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
--no-verbose && \  
bash Miniconda3-latest-Linux-x86_64.sh -b -p /conda && \  
rm Miniconda*.sh  

