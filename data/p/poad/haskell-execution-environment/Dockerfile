FROM debian:stretch-slim  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV HASKELL_VERSION "lts-11.12"  
ENV PATH ${PATH}:/usr/local/bin/:$HOME/.local/bin:$HOME/.stack  
  
USER root  
WORKDIR /root/  
  
ENV PATH /root/.local/bin:${PATH}  
  
VOLUME /root/projects  
  
RUN apt-get -qq update && \  
apt-get -qq -y upgrade && \  
apt-get install -qq -y --no-install-recommends apt-transport-https gnupg
dirmngr curl wget software-properties-common && \  
curl -sSL https://get.haskellstack.org/ | sh && \  
curl -L https://www.stackage.org/stack/linux-x86_64 | \  
tar xz --wildcards --strip-components=1 -C /usr/bin '*/stack' && \  
stack --resolver ${HASKELL_VERSION} config set system-ghc --global true && \  
stack --resolver ${HASKELL_VERSION} install gtk2hs-buildtools --fast -j 4 && \  
apt-get update && \  
apt-get install -qq -y --no-install-recommends \  
apt-utils \  
build-essential \  
ca-certificates \  
g++ gcc git \  
libblas-dev \  
libc6-dev \  
libcairo2-dev \  
libffi-dev \  
liblapack-dev \  
libmagic-dev \  
libpango1.0-dev \  
libsqlite3-0 \  
libsqlite3-dev \  
libtinfo-dev \  
libzmq3-dev \  
make \  
unzip \  
xz-utils \  
zlib1g-dev && \  
apt-get upgrade -qq -y && \  
apt-get autoremove --purge -y && \  
apt-get clean && \  
rm -rf /tmp/* && \  
rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT bash  

