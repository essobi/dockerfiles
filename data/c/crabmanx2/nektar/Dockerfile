FROM crabmanx2/nektar-env  
  
MAINTAINER <Kilian Lackhove> "<kilian@lackhove.de>"  
  
USER nektar:nektar  
WORKDIR /home/nektar  
  
RUN cd /home/nektar/nektar && git pull origin master  
RUN mkdir build && \  
cd build && \  
CC=/usr/bin/clang CXX=/usr/bin/clang++ FC=/usr/bin/gfortran cmake \  
-DCMAKE_BUILD_TYPE:STRING=Debug -DNEKTAR_FULL_DEBUG:BOOL=ON \  
-DNEKTAR_TEST_ALL:BOOL=ON -DNEKTAR_BUILD_TIMINGS:BOOL=ON \  
-DNEKTAR_USE_ARPACK:BOOL=ON -DNEKTAR_USE_FFTW:BOOL=ON \  
-DNEKTAR_USE_VTK:BOOL=ON -DNEKTAR_USE_MPI:BOOL=ON \  
-DNEKTAR_USE_SCOTCH:BOOL=ON -DNEKTAR_USE_PETSC:BOOL=ON \  
-DNEKTAR_USE_HDF5:BOOL=ON \  
-DTHIRDPARTY_BUILD_GSMPI:BOOL=ON -DTHIRDPARTY_BUILD_TINYXML:BOOL=ON \  
-DTHIRDPARTY_BUILD_SCOTCH:BOOL=ON -DNEKTAR_TEST_USE_HOSTFILE=ON \  
-DNEKTAR_USE_MESHGEN:BOOL=ON \  
../nektar/ && \  
CC=/usr/bin/clang CXX=/usr/bin/clang++ FC=/usr/bin/gfortran make boost \  
modmetis-5.1.0 vtk-5.10.1 gsmpi-1.2.1 oce-0.17 arpack-ng-1.0 fftw-3.2.2 \  
scotch-6.0.0 zlib-1.2.7 tetgen-1.5 hdf5-1.8.16 petsc-3.7.2 tinyxml-2.6.2  
RUN cd build && CC=/usr/bin/clang CXX=/usr/bin/clang++ FC=/usr/bin/gfortran
make  
  
  
  

