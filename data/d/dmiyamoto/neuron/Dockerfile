FROM ubuntu:16.04  
  
MAINTAINER Daisuke Miyamoto miyamoto@brain.imi.i.u-tokyo.ac.jp  
  
ARG NRN_VERSION="7.4"  
ARG NRN_ARCH="x86_64"  
  
RUN apt-get update \  
&& apt-get install -y \  
locales \  
wget \  
gcc \  
g++ \  
build-essential \  
libncurses-dev \  
python \  
libpython-dev \  
cython \  
&& mkdir work \  
&& cd work \  
&& wget
http://www.neuron.yale.edu/ftp/neuron/versions/v${NRN_VERSION}/nrn-${NRN_VERSION}.tar.gz
\  
&& tar xvzf nrn-${NRN_VERSION}.tar.gz \  
&& cd nrn-${NRN_VERSION} \  
&& ./configure --prefix=`pwd` --without-iv --with-nrnpython=/usr/bin/python \  
&& make \  
&& make install \  
&& rm -rf /var/lib/apt/lists/* \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8 \  
&& apt-get clean  
  
ENV LANG en_US.utf8  
  
# CMD /work/nrn-7.4/x86_64/bin/nrniv -python  

