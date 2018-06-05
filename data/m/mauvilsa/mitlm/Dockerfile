FROM library/ubuntu:16.04  
  
MAINTAINER Mauricio Villegas <mauricio_ville@yahoo.com>  
  
ENV DEBIAN_FRONTEND=noninteractive  
SHELL ["/bin/bash", "-c"]  
  
### Install build pre-requisites ###  
RUN apt-get update --fix-missing \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
build-essential \  
gfortran \  
automake \  
autoconf \  
autoconf-archive \  
libtool \  
wget \  
  
### Compile and install mitlm ###  
&& cd /tmp \  
&& wget https://github.com/mitlm/mitlm/archive/v0.4.2.tar.gz \  
&& tar xzf v0.4.2.tar.gz \  
&& cd mitlm-0.4.2 \  
&& ./autogen.sh \  
&& ./configure \  
&& make -j$(nproc) \  
&& make install \  
  
### Remove build-only and install runtime software ###  
&& cd \  
&& rm -rf /tmp/* \  
&& apt-get purge -y \  
ca-certificates \  
build-essential \  
gfortran \  
automake \  
autoconf \  
autoconf-archive \  
libtool \  
wget \  
&& apt-get install -y --no-install-recommends \  
libgfortran3 \  
&& apt-get autoremove -y \  
&& apt-get purge -y $(dpkg -l | awk '{if($1=="rc")print $2}') \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY mitlm-docker /usr/local/bin  

