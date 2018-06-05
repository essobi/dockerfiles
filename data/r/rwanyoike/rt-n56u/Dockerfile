FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
autoconf \  
automake \  
bison \  
build-essential \  
ca-certificates \  
flex \  
gawk \  
gettext \  
git \  
gperf \  
libgmp3-dev \  
libmpc-dev \  
libmpfr-dev \  
libtool \  
pkg-config \  
sudo \  
texinfo \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /opt  
  
# The rt-n56u project  
RUN git clone --depth=1 https://bitbucket.org/padavan/rt-n56u.git  
  
# Build the toolchain  
RUN cd rt-n56u/toolchain-mipsel \  
&& ./clean_sources \  
&& ./build_toolchain  

