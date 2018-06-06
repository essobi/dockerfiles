# DO NOT EDIT, This Dockerfile is generated from
./tools/90_generate_dev_Dockerfile.sh  
FROM bjodah/bjodahimg16:v1.3  
MAINTAINER Björn Dahlgren <bjodah@DELETEMEgmail.com>  
RUN \  
cd /tmp && \  
for FNAME in miniconda3.sh boost_1_65_0.tar.bz2 ; do \  
curl -LOs
"http://hera.physchem.kth.se/~repo/bjodahimg16dev/v1.3/blobs/$FNAME"; \  
done && \  
bash miniconda3.sh -b -p /opt/miniconda3 && \  
tar xjf boost_*.tar.bz2 && cd boost* && ./bootstrap.sh && ./b2 -j 2
--prefix=/opt/$(basename $PWD) install && cd \- && \  
rm miniconda3.sh boost_1_65_0.tar.bz2 && \  
wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key|sudo apt-key add - && \  
echo "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-5.0 main" | tee -a
/etc/apt/sources.list && \  
apt-get update && apt-get --quiet --assume-yes --no-install-recommends install
valgrind doxygen scons xorg-dev libgl1-mesa-dev libsdl2-dev libsdl2-ttf-dev
libsdl2-net-dev libsdl2-mixer-dev libsdl2-image-dev libsdl2-gfx-dev \  
clang-5.0 libllvm5.0 lldb-5.0 llvm-5.0 llvm-5.0-dev llvm-5.0-runtime clang-
format-5.0 python-clang-5.0 && \  
PATH=/opt/miniconda3/bin:$PATH conda config --set always_yes yes && \  
PATH=/opt/miniconda3/bin:$PATH conda config --set changeps1 no && \  
PATH=/opt/miniconda3/bin:$PATH conda config --set show_channel_urls True && \  
PATH=/opt/miniconda3/bin:$PATH conda config --add channels conda-forge && \  
PATH=/opt/miniconda3/bin:$PATH conda install \  
conda-build python=3.6 gmp numpy scipy matplotlib cython cmake gsl numba \  
pytest ipywidgets mpmath xz tk mpfr openssl sundials sympy pip sqlite && \  
PATH=/opt/miniconda3/bin:$PATH conda clean -t && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

