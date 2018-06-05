FROM ubuntu:trusty  
  
# https://github.com/ampervue/docker-python27-ffmpeg  
# https://hub.docker.com/r/dkarchmervue/python27-ffmpeg/  
  
MAINTAINER David Karchmer <dkarchmer@ampervue.com>  
  
#####################################################################  
#  
# A Docker image with everything needed to run Python-27  
# This is a base image for:  
# - https://github.com/ampervue/docker-python27-ffmpeg  
# - https://github.com/ampervue/docker-python27-opencv  
#  
# Image based on Ubuntu:14.04  
#  
# with  
# - Latest Python 2.7 (build)  
# - ImageMagick  
#  
# plus a bunch of build/web essentials  
#  
#####################################################################  
  
ENV PYTHON_VERSION 2.7.11  
ENV PYTHON_PIP_VERSION 8.0.2  
ENV YASM_VERSION 1.3.0  
ENV NUM_CORES 4  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
RUN apt-get -qq remove ffmpeg  
# remove several traces of python  
RUN apt-get purge -y python.*  
  
# Add the following two dependencies if you want to use --enable-gnutls in
FFPMEG: gnutls-bin  
RUN echo deb http://archive.ubuntu.com/ubuntu trusty universe multiverse >>
/etc/apt/sources.list; \  
apt-get update -qq && apt-get install -y --force-yes \  
ant \  
autoconf \  
automake \  
build-essential \  
curl \  
checkinstall \  
cmake \  
default-jdk \  
f2c \  
gfortran \  
git \  
g++ \  
imagemagick \  
libass-dev \  
libatlas-base-dev \  
libavcodec-dev \  
libavformat-dev \  
libcnf-dev \  
libfaac-dev \  
libfreeimage-dev \  
libjpeg-dev \  
libjasper-dev \  
libgnutls-dev \  
liblapack3 \  
libmp3lame-dev \  
libpq-dev \  
libpng-dev \  
libssl-dev \  
libtheora-dev \  
libtiff4-dev \  
libtool \  
libxine-dev \  
libxvidcore-dev \  
libv4l-dev \  
libvorbis-dev \  
mercurial \  
openssl \  
pkg-config \  
postgresql-client \  
supervisor \  
wget \  
unzip; \  
apt-get clean  
  
# gpg: key 18ADD4FF: public key "Benjamin Peterson <benjamin@python.org>"
imported  
ENV GPG_KEY C01E1CAD5EA2C4F0B8E3571504C367C218ADD4FF  
  
RUN set -ex \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY" \  
&& curl -fSL
"https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz"
-o python.tar.xz \  
&& curl -fSL
"https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz.asc"
-o python.tar.xz.asc \  
&& gpg --verify python.tar.xz.asc \  
&& mkdir -p /usr/src/python \  
&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \  
&& rm python.tar.xz* \  
&& cd /usr/src/python \  
&& ./configure --enable-shared --enable-unicode=ucs4 \  
&& make -j$(nproc) \  
&& make install \  
&& ldconfig \  
&& curl -fSL 'https://bootstrap.pypa.io/get-pip.py' | python2 \  
&& pip install --no-cache-dir --upgrade pip==$PYTHON_PIP_VERSION \  
&& find /usr/local \  
\\( -type d -a -name test -o -name tests \\) \  
-o \\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
-exec rm -rf '{}' \+ \  
&& rm -rf /usr/src/python  
  
# install "virtualenv", since the vast majority of users of this image will
want it  
RUN pip install --no-cache-dir virtualenv  
  
WORKDIR /usr/local/src  
  
RUN curl -Os
http://www.tortall.net/projects/yasm/releases/yasm-${YASM_VERSION}.tar.gz \  
&& tar xzvf yasm-${YASM_VERSION}.tar.gz  
  
  
# Build YASM  
# =================================  
WORKDIR /usr/local/src/yasm-${YASM_VERSION}  
RUN ./configure \  
&& make -j ${NUM_CORES} \  
&& make install  
# =================================  
  
  
# Remove all tmpfile and cleanup  
# =================================  
WORKDIR /usr/local/  
RUN rm -rf /usr/local/src  
RUN apt-get autoremove -y; apt-get clean -y  
# =================================  
  
# Setup a working directory to allow for  
# docker run --rm -ti -v ${PWD}:/work ...  
# =======================================  
RUN mkdir /work  
WORKDIR /work  
  

