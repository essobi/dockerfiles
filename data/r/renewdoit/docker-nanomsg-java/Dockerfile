FROM renewdoit/docker-clj-build:1.0  
RUN \  
NANOMSG_VERSION=0.8-beta; \  
BUILD_PACKAGES="build-essential"; \  
REMOVE_PACKAGES="binutils build-essential bzip2 cpp cpp-4.9 \  
dpkg-dev fakeroot g++ g++-4.9 gcc \  
gcc-4.9 libalgorithm-diff-perl libalgorithm-diff-xs-perl \  
libalgorithm-merge-perl libasan1 libatomic1 libc-dev-bin libc6-dev \  
libcilkrts5 libcloog-isl4 libdpkg-perl libfakeroot libfile-fcntllock-perl \  
libgcc-4.9-dev libgomp1 libisl10 libitm1 liblsan0 libmpc3 libmpfr4 \  
libquadmath0 libstdc++-4.9-dev libtimedate-perl libtsan0 libubsan0 \  
linux-libc-dev make manpages manpages-dev patch xz-utils"; \  
apt-get update && apt-get install -y $BUILD_PACKAGES && \  
curl -L0k
https://github.com/nanomsg/nanomsg/releases/download/$NANOMSG_VERSION/nanomsg-$NANOMSG_VERSION.tar.gz
| tar xz && \  
cd nanomsg-$NANOMSG_VERSION && \  
./configure && \  
make && make check && make install && \  
echo /usr/local/lib > /etc/ld.so.conf.d/usr-local.conf; \  
ldconfig; \  
cd .. && rm -rf nanomsg-$NANOMSG_VERSION; \  
apt-get purge -y $BUILD_PACKAGES $REMOVE_PACKAGES && rm -rf
/var/lib/apt/lists/*;  

