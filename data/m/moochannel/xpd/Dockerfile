FROM ubuntu:xenial  
  
# Change APT source  
# RUN \  
# sed -i".bak" \  
# "s@http://archive\\.ubuntu\\.com@http://ftp\\.riken\\.go\\.jp/Linux/ubuntu@"
\  
# /etc/apt/sources.list  
# Install gosu  
ENV GOSU_VERSION 1.10  
RUN set -ex; \  
\  
fetchDeps=' \  
ca-certificates \  
wget \  
'; \  
apt-get update; \  
apt-get install -y --no-install-recommends $fetchDeps; \  
rm -rf /var/lib/apt/lists/*; \  
\  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \  
wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch";
\  
wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc";
\  
\  
# verify the signature  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4; \  
gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \  
rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc; \  
\  
chmod +x /usr/local/bin/gosu; \  
# verify that the binary works  
gosu nobody true; \  
\  
apt-get purge -y --auto-remove $fetchDeps  
  
# Basic settings  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
apt-utils && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
language-pack-en tzdata software-properties-common && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
update-locale LANG=en_US.UTF-8  
ENV \  
XPD_DATA_DIR=/home/wallet/.XP  
  
# Create a normal user  
RUN \  
useradd -d /home/wallet -m -s /bin/bash wallet  
  
# Prepare for build XPd  
WORKDIR /usr/src  
RUN \  
apt-add-repository ppa:bitcoin/bitcoin -y && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
build-essential libssl-dev libdb4.8-dev libdb4.8++-dev libboost-all-dev \  
libqrencode-dev ca-certificates git curl unzip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Build XPd  
ARG XPD_VER=1.1.0  
RUN \  
git clone https://github.com/eXperiencePoints/XPCoin -b ${XPD_VER} && \  
cd XPCoin/src && \  
make -f makefile.unix && \  
chmod +x XPd && \  
mv XPd /usr/local/bin && \  
cd /usr/src && \  
rm -fr /usr/src/XPCoin  
  
# Place an entrypoint script  
COPY docker-entrypoint.sh /  
RUN \  
chmod +x /docker-entrypoint.sh && \  
gosu wallet mkdir ${XPD_DATA_DIR}  
  
# RUN \  
# apt-get update && \  
# DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
# vim sudo && \  
# apt-get clean && \  
# rm -rf /var/lib/apt/lists/* && \  
# echo "wallet ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/wallet  
USER wallet  
WORKDIR /home/wallet  
VOLUME ["${XPD_DATA_DIR}"]  
EXPOSE 28191 28192  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/usr/local/bin/XPd", "--printtoconsole"]  

