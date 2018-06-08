FROM fdiskyou/afl-qemu:0.1  
MAINTAINER rui@deniable.org  
  
# check https://hub.docker.com/u/fdiskyou/ for more information  
ENV WRKSRC /opt  
ENV BIN_DIR ~/bin  
ENV GOPATH $WRKSRC/go  
ENV DYNAMO_DOWNLOAD
https://github.com/DynamoRIO/dynamorio/releases/download/release_7_0_0_rc1/DynamoRIO-
Linux-7.0.0-RC1.tar.gz  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN dpkg --add-architecture i386 && \  
apt-get update && apt-get -y upgrade && \  
apt-get -y install git cmake libelf-dev libelf1 libiberty-dev libboost-all-dev
golang \  
libtool autoconf pkg-config python-dev lzma lzma-dev sudo liblzma-dev liblz-
dev \  
liblz1 valgrind valgrind-dbg gdb htop nasm binwalk binutils strace ltrace
unzip \  
libtool-bin screen python3-dev python-pip python3-pip radare2 radare2-plugins
&& \  
git clone https://github.com/pwndbg/pwndbg.git $WRKSRC/pwndbg && cd
$WRKSRC/pwndbg && ./setup.sh && \  
git clone https://github.com/jfoote/exploitable.git $WRKSRC/exploitable && cd
$WRKSRC/exploitable && python setup.py install && \  
git clone https://github.com/fuzzamos/checksec.sh.git $WRKSRC/checksec && \  
git clone https://github.com/fuzzamos/fuzzdiff.git $WRKSRC/fuzzdiff && \  
git clone https://github.com/rc0r/afl-utils.git $WRKSRC/afl-utils && \  
cd $WRKSRC/afl-utils && python setup.py install && \  
mkdir -p $GOPATH && echo "GOPATH=$WRKSRC/go" >> .bashrc && echo
"PATH=$PATH:$GOPATH/bin" >> .bashrc && \  
go get -u github.com/bnagy/crashwalk/cmd/... && \  
cd $WRKSRC && mkdir -p $WRKSRC/dynamorio && mkdir -p $BIN_DIR && \  
curl -L $DYNAMO_DOWNLOAD | tar -zxf - -C dynamorio --strip 1 && \  
ln -s $WRKSRC/dynamorio/drmemory/bin64/drmemory $BIN_DIR/ && \  
ln -s $WRKSRC/dynamorio/bin64/drrun $BIN_DIR/ && \  
ln -s $WRKSRC/dynamorio/tools/bin64/drcov2lcov $BIN_DIR/ && \  
ln -s $WRKSRC/dynamorio/tools/bin64/genhtml $BIN_DIR/ && \  
apt-get -qy clean autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["/bin/bash"]  

