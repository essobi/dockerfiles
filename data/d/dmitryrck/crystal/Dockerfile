from ubuntu  
  
env DEBIAN_FRONTEND noninteractive  
  
run sed -i "/deb-src/d" /etc/apt/sources.list && \  
apt-get update && \  
apt-get install --yes \  
libbsd-dev \  
libedit-dev \  
libevent-core-2.0-5 \  
libevent-dev \  
libevent-extra-2.0-5 \  
libevent-openssl-2.0-5 \  
libevent-pthreads-2.0-5 \  
libgmp-dev \  
libgmpxx4ldbl \  
libssl-dev \  
libxml2-dev \  
libyaml-dev \  
libreadline-dev \  
automake \  
libtool \  
git \  
llvm \  
libpcre3-dev \  
build-essential \  
curl libatomic-ops-dev pkg-config && \  
rm -rf /var/lib/apt/lists/*  
  
run curl -sSL "https://github.com/crystal-
lang/crystal/releases/download/0.21.1/crystal-0.21.1-1-linux-x86_64.tar.gz" |
tar xfz - -C /opt && \  
ln -s /opt/crystal-0.21.1-1/bin/crystal /usr/local/bin/crystal  
  
run git clone \--depth=1 https://github.com/ivmai/bdwgc.git /usr/src/bdwgc  
workdir /usr/src/bdwgc  
run ./autogen.sh && ./configure --prefix=/usr && \  
make -j && make check && make install  
  
run git clone https://github.com/crystal-lang/crystal.git /opt/crystal  
workdir /opt/crystal  
run git checkout 0.22.0 && make threads=1 && \  
rm /usr/local/bin/crystal && ln -s /opt/crystal/bin/crystal
/usr/local/bin/crystal  
  
run git clone \--depth=1 https://github.com/crystal-lang/shards.git
/usr/src/shards  
workdir /usr/src/shards  
run make release && cp bin/shards /usr/local/bin  

