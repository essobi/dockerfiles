FROM debian:jessie  
  
MAINTAINER danielguerra, https://github.com/danielguerra  
  
#set the path  
ENV PATH /usr/local/bro/bin:/scripts:$PATH  
RUN echo "export PATH=$PATH:/usr/local/bro/bin:/scripts" > /root/.profile  
  
# Install Bro + Required Dependencies  
RUN buildDeps='build-essential \  
autoconf \  
install-info \  
libgoogle-perftools-dev \  
libcurl3-dev \  
libgeoip-dev \  
libpcap-dev \  
libssl-dev \  
python-dev \  
zlib1g-dev \  
libedit-dev \  
doxygen \  
git-core \  
cmake \  
make \  
g++ \  
gcc \  
libpcre3-dev \  
python-setuptools \  
libsnappy-dev \  
libbz2-dev \  
devscripts \  
libjemalloc-dev \  
libjemalloc1-dbg ' \  
&& set -x \  
&& echo "[INFO] Installing Dependancies..." \  
&& apt-get -qq update \  
&& apt-get -qq upgrade \  
&& apt-get install -yq $buildDeps \  
supervisor \  
tcpdump \  
apache2 \  
libapache2-mod-php5 \  
libjemalloc1 \  
amqp-tools \  
locales \  
vim \  
xinetd \  
php5-curl \  
sendmail \  
bison \  
flex \  
gawk \  
curl \  
geoip-database \  
geoip-database-extra \  
wget \  
ca-certificates \  
openssh-server --no-install-recommends \  
&& export LANGUAGE="en_US:en" \  
&& export LANG="en_US.UTF-8" \  
&& locale-gen "en_US.UTF-8" \  
&& sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \  
&& dpkg-reconfigure -f noninteractive locales \  
&& cd /tmp \  
&& git clone --recursive https://github.com/kohler/ipsumdump.git \  
&& cd /tmp/ipsumdump \  
&& /bin/bash ./configure --enable-all-elements ;make; make install \  
&& cd /tmp \  
&& wget
http://downloads.sourceforge.net/project/swig/swig/swig-3.0.10/swig-3.0.10.tar.gz
\  
&& tar xvfz swig-3.0.10.tar.gz \  
&& cd /tmp/swig-3.0.10 \  
&& ./configure \  
&& make \  
&& make install \  
&& cd /tmp \  
&& git clone --recursive https://github.com/facebook/rocksdb.git \  
&& cd /tmp/rocksdb \  
&& export CFLAGS="$CFLAGS -fPIC" && export CXXFLAGS="$CXXFLAGS -fPIC" \  
&& make shared_lib \  
&& make install \  
&& export CFLAGS="" && export CXXFLAGS="" \  
&& cd /tmp \  
&& git clone --recursive --branch 0.14.2 https://github.com/actor-
framework/actor-framework.git \  
&& cd /tmp/actor-framework \  
&& ./configure --no-examples --no-benchmarks --no-opencl \  
&& make \  
&& make install \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

