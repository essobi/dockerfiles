FROM ubuntu:xenial as build  
  
RUN apt-get -y update && apt-get install -y apt-utils && \  
apt-get install -y -qq -o=Dpkg::Use-Pty=0 build-essential gfortran zlib1g-dev
\  
libhdf5-dev libcurl4-openssl-dev libboost-dev cmake wget python  
  
#  
# build PETSc with mpich for static linking  
#  
RUN mkdir /usr/local/petsc && \  
cd /usr/local/petsc && \  
wget http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-3.7.7.tar.gz &&
\  
tar xzf petsc-3.7.7.tar.gz && \  
cd petsc-3.7.7 && \  
./configure \--with-shared-libraries=0 --download-fblaslapack=1 --with-
debugging=1 --download-mpich && \  
make PETSC_DIR=/usr/local/petsc/petsc-3.7.7 PETSC_ARCH=arch-linux2-c-debug all  
  
ENV PETSC_DIR=/usr/local/petsc/petsc-3.7.7 \  
PETSC_ARCH=arch-linux2-c-debug  
  
COPY . /vcellroot  
  
#  
# build most solvers, and FiniteVolume without PETSc (FiniteVolume_x64)  
#  
RUN mkdir -p /vcellroot/build/bin  
WORKDIR /vcellroot/build  
  
RUN /usr/bin/cmake \  
-DOPTION_TARGET_MESSAGING=ON \  
-DOPTION_TARGET_PARALLEL=OFF \  
-DOPTION_TARGET_PETSC=OFF \  
-DOPTION_TARGET_CHOMBO2D_SOLVER=OFF \  
-DOPTION_TARGET_CHOMBO3D_SOLVER=OFF \  
-DOPTION_TARGET_SMOLDYN_SOLVER=ON \  
-DOPTION_TARGET_FV_SOLVER=ON \  
-DOPTION_TARGET_STOCHASTIC_SOLVER=ON \  
-DOPTION_TARGET_NFSIM_SOLVER=ON \  
-DOPTION_TARGET_MOVINGBOUNDARY_SOLVER=ON \  
-DOPTION_TARGET_SUNDIALS_SOLVER=ON \  
-DOPTION_TARGET_HY3S_SOLVERS=OFF \  
.. && \  
make  
  
#  
# build FiniteVolume with PETSc (FiniteVolume_PETSc_x64)  
#  
RUN mkdir -p /vcellroot/build_PETSc/bin  
WORKDIR /vcellroot/build_PETSc  
  
RUN /usr/bin/cmake \  
-DOPTION_TARGET_MESSAGING=ON \  
-DOPTION_TARGET_PARALLEL=OFF \  
-DOPTION_TARGET_PETSC=ON \  
-DOPTION_TARGET_CHOMBO2D_SOLVER=OFF \  
-DOPTION_TARGET_CHOMBO3D_SOLVER=OFF \  
-DOPTION_TARGET_SMOLDYN_SOLVER=OFF \  
-DOPTION_TARGET_FV_SOLVER=ON \  
-DOPTION_TARGET_STOCHASTIC_SOLVER=OFF \  
-DOPTION_TARGET_NFSIM_SOLVER=OFF \  
-DOPTION_TARGET_MOVINGBOUNDARY_SOLVER=OFF \  
-DOPTION_TARGET_SUNDIALS_SOLVER=OFF \  
-DOPTION_TARGET_HY3S_SOLVERS=OFF \  
.. && \  
make  
  
  
FROM ubuntu:xenial  
  
RUN apt-get -y update && apt-get install -y apt-utils && \  
apt-get install -y -qq -o=Dpkg::Use-Pty=0 gcc gfortran zlib1g \  
libhdf5-10 libhdf5-cpp-11 libcurl4-openssl-dev  
  
COPY \--from=build /vcellroot/build/bin /vcellbin  
COPY \--from=build /vcellroot/build_PETSc/bin/FiniteVolume_PETSc_x64
/vcellbin/  
WORKDIR /vcellbin  
ENV PATH=/vcellbin:$PATH  

