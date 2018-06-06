FROM ubuntu:16.04  
LABEL maintainer="Stephen Roberts"  
RUN apt-get update && \  
apt-get install -y build-essential curl libgmp-dev libmpc-dev libmpfr-dev \  
gcc-multilib numactl gfortran tcl tcl-dev  
RUN curl -SL
http://sourceforge.net/projects/modules/files/Modules/modules-4.0.0/modules-4.0.0.tar.gz
| tar -xzC /usr/local/src && \  
cd /usr/local/src/modules-4.0.0 && \  
./configure --prefix=/opt/modules-4.0.0 && \  
make && \  
make install && \  
echo "source /opt/modules-4.0.0/init/bash_completion" >> /etc/skel/.bashrc  
ENV MODULESHOME=/opt/modules-4.0.0/ \  
MODULE_VERSION=4.0.0 \  
MODULEPATH=/opt/modules-4.0.0/modulefiles:/opt/combos/modulefiles  
COPY modulefiles /opt/combos/modulefiles  
  
# Build GNU compilers. Note: For final setup, this should also include 6.3.0  
#RUN curl -SL ftp://ftp.gnu.org/gnu/gcc/gcc-7.2.0/gcc-7.2.0.tar.gz | tar -xzC
/usr/local/src && \  
# cd /usr/local/src/gcc-7.2.0 && \  
# ./contrib/download_prerequisites && \  
# mkdir /usr/local/src/gcc-7.2.0_build && \  
# cd /usr/local/src/gcc-7.2.0_build && \  
# /usr/local/src/gcc-7.2.0/configure --prefix=/opt/gcc-7.2.0 --enable-
languages=c,c++,fortran && \  
# make -j 2 && \  
# make install && \  
# rm -rf /usr/local/src/gcc-7.2.0_build  
# Download MPI Libraries  
# Seperate download/compile stages to allow compiler/mpi combinations  
RUN curl -SL http://www.mpich.org/static/downloads/3.2.1/mpich-3.2.1.tar.gz |
tar -xzC /usr/local/src && \  
curl -SL https://www.open-
mpi.org/software/ompi/v3.0/downloads/openmpi-3.0.0.tar.gz | tar -xzC
/usr/local/src  
  
# Compile MPI Libraries  
RUN eval $(/usr/bin/tclsh /opt/modules-4.0.0/libexec/modulecmd.tcl sh load
compilers/gnu/5.4.0-system) && \  
mkdir /usr/local/src/mpich-3.2.1_${COMPILER_NAME}-${COMPILER_VER}_build && \  
cd /usr/local/src/mpich-3.2.1_${COMPILER_NAME}-${COMPILER_VER}_build && \  
/usr/local/src/mpich-3.2.1/configure
--prefix=/opt/mpich-3.2.1_${COMPILER_NAME}-${COMPILER_VER} \--enable-debuginfo
&& \  
make -j 2 && \  
make install && \  
rm -rf /usr/local/src/mpich-3.2.1_${COMPILER_NAME}-${COMPILER_VER}_build  
RUN eval $(/usr/bin/tclsh /opt/modules-4.0.0/libexec/modulecmd.tcl sh load
compilers/gnu/5.4.0-system) && \  
mkdir /usr/local/src/openmpi-3.0.0_${COMPILER_NAME}-${COMPILER_VER}_build && \  
cd /usr/local/src/openmpi-3.0.0_${COMPILER_NAME}-${COMPILER_VER}_build && \  
/usr/local/src/openmpi-3.0.0/configure
--prefix=/opt/openmpi-3.0.0_${COMPILER_NAME}-${COMPILER_VER} && \  
make -j 2 && \  
make install && \  
rm -rf /usr/local/src/openmpi-3.0.0_${COMPILER_NAME}-${COMPILER_VER}_build  

