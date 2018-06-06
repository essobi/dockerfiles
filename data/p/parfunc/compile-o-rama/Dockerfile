  
# Name this with the tag "compile-o-rama"  
# (*) Haskell, GHC 8.0.2: we bake this in (goes in /opt/ghc)  
# ======================================================================  
FROM fpco/stack-build:lts-9.14  
# (*) Mlton, Ocaml, gcc to /usr/bin  
# ======================================================================  
RUN apt-get update && apt-get -y install mlton ocaml-native-compilers gcc time  
  
  
# (*) Clang, LLVM  
# ======================================================================  
## LLVM and CLANG 3.9  
RUN wget -O - http://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - && \  
apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-3.9
main" && \  
apt-get update && \  
apt-get -y install clang-3.9 llvm-3.9  
# (*) Chez Scheme to /usr/bin/scheme  
# ======================================================================  
# TODO: Check SHA like Nix does:  
ENV CHEZ_VER 9.4  
RUN cd / && wget -nv
https://github.com/cisco/ChezScheme/archive/v${CHEZ_VER}.tar.gz && \  
tar xf v${CHEZ_VER}.tar.gz && rm -f v${CHEZ_VER}.tar.gz  
RUN cd /ChezScheme-${CHEZ_VER}/ && ./configure && time make install  
  
# ADD ./deps /tree-velocity/BintreeBench/deps  
# (*) Rust  
# ======================================================================  
ENV RUST_VER 1.25.0  
# Having problems on hive, disabling rustup: [2016.11.02]  
# RUN deps/rustup.sh --yes --revision=1.12.0  
# wget --progress=dot:giga https://static.rust-
lang.org/dist/rust-${RUST_VER}-x86_64-unknown-linux-gnu.tar.gz && \  
RUN mkdir /tmp/rust && cd /tmp/rust && \  
curl -O https://static.rust-lang.org/dist/rust-${RUST_VER}-x86_64-unknown-
linux-gnu.tar.gz && \  
tar xf rust-${RUST_VER}-x86_64-unknown-linux-gnu.tar.gz && \  
cd rust-${RUST_VER}-x86_64-unknown-linux-gnu && \  
./install.sh && \  
cd / && rm -rf /tmp/rust  
  
  
# (*) Racket to /racket  
# ======================================================================  
# Xenial is Ubuntu 16.04. Getting newer currently needs Zesty/Artful.  
RUN add-apt-repository ppa:plt/racket && apt-get update && \  
apt-get -y install racket=6.12+ppa1-1~xenial2  
  
# Or can do it this way:  
# ENV RACKET_VER 6.11  
# RUN cd /tmp/ && \  
# wget --progress=dot:giga http://download.racket-
lang.org/releases/${RACKET_VER}/installers/racket-${RACKET_VER}-x86_64-linux.sh
&& \  
# chmod +x racket-${RACKET_VER}-x86_64-linux.sh && \  
# ./racket-${RACKET_VER}-x86_64-linux.sh --in-place --dest /racket/ && \  
# ln -s /racket/bin/* /usr/local/bin/ && \  
# rm -rf racket-${RACKET_VER}-x86_64-linux.sh  
# (*) Manticore to /usr/local/bin and /manticore  
# ======================================================================  
RUN cd /usr/local && \  
mkdir smlnj && cd smlnj && \  
wget http://smlnj.cs.uchicago.edu/dist/working/110.81/config.tgz && \  
tar -xvf config.tgz && \  
rm -rf config.tgz && \  
apt-get update && \  
apt-get -y install wget lynx curl && \  
apt-get -y install gcc-multilib g++-multilib && \  
apt-get -y install lib32ncurses5 lib32z1 && \  
config/install.sh && \  
cd / && \  
git clone https://github.com/ManticoreProject/manticore.git && \  
cd manticore && \  
autoheader -Iconfig && autoconf -Iconfig && \  
export SMLNJ_CMD=/usr/local/smlnj/bin/sml && \  
./configure && \  
make install -j && \  
cd /  
  
  
# TODO: .NET core  
# TODO: multimlton  
# TODO: Java, Scala  
# Add your compilers here (or inherit from this with FROM):  
# ------------------------------------------------------------  
#
==================================================================================================  
# DISTRIBUTED-MEMORY LANGUAGE SUPPORT  
#
==================================================================================================  
#  
# What's below adds support for distributed, multi-node compilers and  
# runtimes.  
# For "lockfile" command:  
# RUN apt install -y procmail  
# Above is overkill. Other hack for lockfile command:  
RUN apt-get install -y lockfile-progs  
ADD scripts/lockfile /usr/bin/lockfile  
  
# OCR: Open community runtime  
# ======================================================================  
# As of May 3, 2018, the link to ocr repo is dead. Remove it for now.  
#RUN mkdir /ocr && \  
# git clone --depth 1 -b OCRv1.2.0 https://xstack.exascale-
tech.com/git/public/ocr.git /ocr/lib  
#  
#RUN cd /ocr/lib/ocr && \  
# OCR_TYPE=x86 make all -j  
#  
#RUN export OCR_INSTALL=/usr/; \  
# cd /ocr/lib/ocr && \  
# OCR_TYPE=x86 make install  
# HPX-5:  
# =====================================================================  
# link to HPX-5 is also gone.  
#ENV HPX5_VER 4.1.0  
#RUN mkdir /tmp/hpx5 && cd /tmp/hpx5 && \  
# wget -nv http://hpx.crest.iu.edu/release/hpx-${HPX5_VER}.tar.gz && \  
# tar xf hpx-${HPX5_VER}.tar.gz && rm -f hpx-${HPX5_VER}.tar.gz && \  
# cd hpx-${HPX5_VER}/hpx && \  
# ./configure --enable-parallel-config --prefix=/hpx5 && \  
# make -j && \  
# make install && \  
# cd / && rm -rf /tmp/hpx5  
#ENV LD_LIBRARY_PATH /hpx5/lib  
#ENV INCLUDE /hpx5/include  
#ENV PKG_CONFIG_PATH /hpx5/lib/pkgconfig  
# CHAPEL  
# =====================================================================  
ENV CHPL_VER 1.16.0  
RUN mkdir /tmp/chapel && cd /tmp/chapel && \  
wget -nv https://github.com/chapel-
lang/chapel/releases/download/${CHPL_VER}/chapel-${CHPL_VER}-1.tar.gz && \  
tar xf chapel-${CHPL_VER}-1.tar.gz && rm -f chapel-${CHPL_VER}-1.tar.gz && \  
cd chapel-${CHPL_VER} && \  
./configure && make && make install && \  
cd / && rm -rf /tmp/chapel  
  
  
# CHARM++  
# ====================================================================  
ENV CHARM_VER 6.8.2  
ENV CHARM_HOME /usr/local/charm  
RUN mkdir /charm && cd /charm && \  
wget -nv http://charm.cs.illinois.edu/distrib/charm-${CHARM_VER}.tar.gz && \  
tar xf charm-${CHARM_VER}.tar.gz && rm -f charm-${CHARM_VER}.tar.gz && \  
cd charm-v${CHARM_VER} && \  
./build charm++ multicore-linux-x86_64 --with-production -j8
--destination=${CHARM_HOME}  

