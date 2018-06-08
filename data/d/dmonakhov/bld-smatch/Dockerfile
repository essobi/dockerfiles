FROM debian:jessie  
MAINTAINER Dmitry Monakhov <dmonakhov@gmail.com>  
  
ADD /entrypoint.sh /entrypoint.sh  
  
RUN \  
apt-get update && apt-get install -y \  
bc \  
ca-certificates \  
curl \  
git \  
gawk \  
kernel-package \  
make \  
libncurses5-dev \  
libssl-dev \  
\--no-install-recommends && \  
echo "Info: Install static checkers, currently sparse belongs to non-free" &&
\  
sed -i 's/main/main non-free/g' /etc/apt/sources.list && \  
apt-get update && apt-get install -y \  
sparse \  
sqlite3 \  
libsqlite3-dev \  
libdbd-sqlite3-perl \  
llvm-dev \  
libedit-dev \  
\--no-install-recommends && \  
mkdir -p /opt && \  
git clone -b dockerimg https://github.com/dmonakhov/smatch /opt/smatch && \  
cd /opt/smatch && \  
INSTALL_PREFIX=/usr make -j `nproc` && \  
INSTALL_PREFIX=/usr make install && \  
cd / && \  
chmod +x /entrypoint.sh && \  
mkdir -p /bld/src && \  
mkdir -p /bld/result && \  
echo "Info: Cleanup build packages" && \  
rm -rf /opt/smatch && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /  
ENTRYPOINT ["/entrypoint.sh"]  
  

