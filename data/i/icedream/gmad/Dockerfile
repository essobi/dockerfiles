FROM ubuntu:yakkety  
  
ARG GMAD_GIT_URL="https://github.com/garrynewman/gmad.git"  
ARG GMAD_VERSION="377f3458bf1ecb8a1a2217c2194773e3c2a2dea0"  
ARG BOOTIL_GIT_URL="https://github.com/garrynewman/bootil.git"  
ARG BOOTIL_VERSION="1d3e321fc2be359e2350205b8c7f1cad2164ee0b"  
COPY bootil-patches/ /usr/src/bootil-patches/  
RUN \  
apt-get update \  
&& apt-get install -y \  
premake4 \  
g++ \  
make \  
git \  
&& apt-mark auto \  
premake4 \  
g++ \  
make \  
git \  
\  
&& git config --global user.email "docker@localhost" \  
&& git config --global user.name "Docker" \  
\  
&& git clone "${BOOTIL_GIT_URL}" /usr/src/bootil \  
&& (cd /usr/src/bootil \  
&& git checkout "${BOOTIL_VERSION}" \  
&& git apply /usr/src/bootil-patches/* \  
&& cd projects \  
&& premake4 gmake \  
&& cd linux/gmake \  
&& make \  
) \  
\  
&& git clone "${GMAD_GIT_URL}" /usr/src/gmad \  
&& (cd /usr/src/gmad \  
&& git checkout "${GMAD_VERSION}" \  
&& premake4 \  
\--outdir="/usr/local/bin/" \  
\--bootil_lib="/usr/src/bootil/lib/linux/gmake/" \  
\--bootil_inc="/usr/src/bootil/include/" \  
gmake \  
&& make -j$(nproc) \  
) \  
\  
&& apt-get autoremove --purge -y \  
&& apt-get clean \  
&& rm -rf \  
/tmp/* \  
/var/tmp/* \  
/var/lib/apt/lists/* \  
/usr/src/*  
  
ENTRYPOINT ["gmad_linux"]  

