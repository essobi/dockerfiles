FROM library/ubuntu:16.04  
  
MAINTAINER Mauricio Villegas <mauricio_ville@yahoo.com>  
  
ENV DEBIAN_FRONTEND=noninteractive  
SHELL ["/bin/bash", "-c"]  
  
### Install build pre-requisites ###  
RUN apt-get update --fix-missing \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
build-essential \  
git \  
subversion \  
zlib1g-dev \  
automake \  
autoconf \  
wget \  
libtool \  
libatlas3-base \  
python \  
python3 \  
  
### Compile and install kaldi from repo ###  
&& git clone --depth 1 https://github.com/kaldi-asr/kaldi.git /tmp/kaldi \  
&& cd /tmp/kaldi/tools \  
&& make -j$(nproc) \  
&& mv openfst/bin/* sctk/bin/* sph2pipe*/sph2pipe /usr/local/bin \  
&& mv openfst/lib/* /usr/local/lib \  
&& mv openfst/include/* /usr/local/include \  
&& rmdir openfst/lib openfst/include \  
&& ln -s /usr/local/lib openfst/lib \  
&& ln -s /usr/local/include openfst/include \  
&& cd ../src \  
&& ./configure --shared \  
&& sed 's|\\( -g # -O0.*\\)| -O3 -DNDEBUG #\1|' -i~ kaldi.mk \  
&& make depend -j$(nproc) \  
&& make -j$(nproc) \  
&& for f in $(find . -type f -executable | grep -F bin/); do echo $f $(file
$f); done | grep 'ELF 64-bit LSB executable' | sed 's| .*||' | xargs mv -t
/usr/local/bin \  
&& mv $(realpath lib/*) /usr/local/lib \  
### Remove build-only software ###  
&& cd \  
&& rm -rf /tmp/kaldi \  
&& apt-get purge -y \  
ca-certificates \  
build-essential \  
git \  
subversion \  
zlib1g-dev \  
automake \  
autoconf \  
wget \  
libtool \  
python \  
python3 \  
&& apt-get autoremove -y \  
&& apt-get purge -y $(dpkg -l | awk '{if($1=="rc")print $2}') \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY kaldi-docker /usr/local/bin  

