FROM alpine:3.5  
LABEL Description="musl build environment for MIPSel"  
LABEL Maintainer="Nils Andreas Svee <me@lochnair.net>"  
  
RUN \  
# Install build dependencies  
apk add \--no-cache \  
\--update-cache \  
autoconf \  
automake \  
bison \  
build-base \  
coreutils \  
curl \  
file \  
flex \  
gawk \  
git \  
gmp-dev \  
libtool \  
mpc1-dev \  
mpfr-dev \  
shadow \  
su-exec \  
texinfo  
  
RUN \  
mkdir /usr/src && \  
cd /usr/src && \  
git clone https://github.com/richfelker/musl-cross-make.git  
  
COPY root/ /  
  
RUN \  
cd /usr/src/musl-cross-make && \  
make -j$(nproc) && \  
make install && \  
rm -rf /usr/src && \  
useradd -m -U -s /bin/sh -u 1234 user && \  
chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

