FROM ubuntu:xenial  
ENV LLVM=5.0  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
. /etc/lsb-release && add-apt-repository "deb
http://apt.llvm.org/$DISTRIB_CODENAME/ llvm-toolchain-$DISTRIB_CODENAME-$LLVM
main" -y && \  
apt-key adv --fetch-keys http://apt.llvm.org/llvm-snapshot.gpg.key && \  
apt-get install -y \  
cmake \  
g++ \  
gfortran \  
git \  
hdf5-tools \  
libblas-dev \  
libboost-all-dev \  
libfftw3-dev \  
libgfortran3 \  
libgmp-dev \  
libhdf5-serial-dev \  
liblapack-dev \  
libopenmpi-dev \  
openmpi-bin \  
openmpi-common \  
openmpi-doc \  
python-dev \  
python-h5py \  
python-jinja2 \  
python-mako \  
python-matplotlib \  
python-mpi4py \  
python-numpy \  
python-scipy \  
python-tornado \  
python-virtualenv \  
python-zmq \  
python-sphinx \  
\  
clang-$LLVM \  
libclang-$LLVM-dev \  
python-clang-$LLVM \  
\  
libnfft3-dev \  
\  
sudo \  
python-pip \  
&& \  
apt-get autoremove --purge -y && \  
apt-get autoclean -y && \  
rm -rf /var/cache/apt/* /var/lib/apt/lists/*  
  
RUN pip install --no-cache-dir notebook==5.* ipython==5.*  
  
ENV CC=clang-$LLVM CXX=clang++-$LLVM  
  
ADD http://releases.llvm.org/5.0.1/libcxx-5.0.1.src.tar.xz /tmp/  
ADD http://releases.llvm.org/5.0.1/libcxxabi-5.0.1.src.tar.xz /tmp/  
RUN mkdir /tmp/build && cd /tmp/build && \  
tar -C /tmp -xf /tmp/libcxx-5.0.1.src.tar.xz && \  
tar -C /tmp -xf /tmp/libcxxabi-5.0.1.src.tar.xz && \  
cmake /tmp/libcxxabi-5.0.1.src -DLLVM_CONFIG_PATH=/usr/bin/llvm-config-$LLVM
-DCMAKE_INSTALL_PREFIX=/usr/lib/llvm-$LLVM
-DLIBCXXABI_LIBCXX_PATH=/tmp/libcxx-5.0.1.src && make -j2 && make install && \  
rm -rf * && \  
cmake /tmp/libcxx-5.0.1.src -DLLVM_CONFIG_PATH=/usr/bin/llvm-config-$LLVM
-DCMAKE_INSTALL_PREFIX=/usr/lib/llvm-$LLVM -DLIBCXX_CXX_ABI=libcxxabi
-DLIBCXX_CXX_ABI_INCLUDE_PATHS=/tmp/libcxxabi-5.0.1.src/include && make -j2
install && \  
rm -rf /tmp/libcxx* /tmp/build  
ENV CXXFLAGS="-stdlib=libc++" LD_LIBRARY_PATH=/usr/lib/llvm-$LLVM/lib  
  
ENV SRC=/src \  
BUILD=/home/build \  
INSTALL=/usr/local \  
PYTHONPATH=/usr/local/lib/python2.7/site-packages \  
CMAKE_PREFIX_PATH=/usr/local/share/cmake  
ARG BUILD_DOC=0  
RUN useradd -d $BUILD -m build  
  
COPY cpp2py $SRC/cpp2py  
WORKDIR $BUILD/cpp2py  
RUN chown build .  
USER build  
RUN cmake $SRC/cpp2py -DCMAKE_INSTALL_PREFIX=$INSTALL
-DLIBCLANG_CXX_FLAGS="-I/usr/lib/llvm-$LLVM/include/c++/v1" && make -j2  
USER root  
RUN make install  
  
COPY triqs $SRC/triqs  
WORKDIR $BUILD/triqs  
RUN chown build .  
USER build  
RUN cmake $SRC/triqs -DCMAKE_INSTALL_PREFIX=$INSTALL
-DBuild_Documentation=$BUILD_DOC
-DCPP2RST_INCLUDE_DIRS=--includes=/usr/lib/llvm-$LLVM/include/c++/v1
-DMATHJAX_PATH="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2" && make
-j2  
USER root  
RUN make install  
  
COPY dft_tools $SRC/dft_tools  
WORKDIR $BUILD/dft_tools  
RUN chown build .  
USER build  
RUN cmake $SRC/dft_tools -DTRIQS_ROOT=$INSTALL
-DBuild_Documentation=$BUILD_DOC && make -j2  
USER root  
RUN make install  
  
COPY cthyb $SRC/cthyb  
WORKDIR $BUILD/cthyb  
RUN chown build .  
USER build  
RUN cmake $SRC/cthyb -DTRIQS_ROOT=$INSTALL && make -j2  
USER root  
RUN make install  
  
WORKDIR /  
RUN rm -rf $SRC $BUILD && userdel build  
ARG NB_USER=triqs  
ARG NB_UID=1000  
RUN useradd -u $NB_UID -m $NB_USER && \  
echo 'triqs ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
ADD https://github.com/TRIQS/tutorials/archive/unstable.tar.gz
/tmp/tutorials.tar.gz  
RUN chown $NB_USER /tmp/tutorials.tar.gz  
USER $NB_USER  
WORKDIR /home/$NB_USER  
ENV CC=clang-$LLVM CXX=clang++-$LLVM  
ENV CPATH=/usr/include/openmpi:/usr/include/hdf5/serial:$CPATH  
RUN tar xzf /tmp/tutorials.tar.gz --one-top-level --strip-components=1 && rm
/tmp/tutorials.tar.gz  
  
EXPOSE 8888  
CMD ["jupyter","notebook","--ip","0.0.0.0"]  

