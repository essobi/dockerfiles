#Version 1.1  
#add the base image  
FROM centos:7  
#install and configure the dependencies  
RUN yum -y install \  
epel-release \  
wget make \  
gcc gcc-c++ \  
gcc-gfortran \  
tcl tcl-devel \  
libtool libtool-ltdl-devel \  
autoconf flex bison pkgconfig \  
expat expat-devel \  
libtool-ltdl-devel \  
netcdf-devel ruby \  
openmpi openmpi-devel.x86_64 \  
openssh-server openssh-clients  
ENV PATH $PATH:/usr/lib64/openmpi/bin  
ENV LD_LIBRARY_PATH /usr/lib64/openmpi/lib:$LD_LIBRARY_PATH  
#download the delft3d package  
WORKDIR /root  
RUN wget
http://lsu.ngchc.org/project/crc/models/delft3d/delft3d-5.01.00.2163.tgz  
RUN tar -zxvf delft3d-5.01.00.2163.tgz  
  
#compile  
WORKDIR delft3d-5.01.00.2163/src  
RUN ./build.sh -gnu  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/root/delft3d-5.01.00.2163/src/lib  
#run test case in parallel  
WORKDIR /root/delft3d-5.01.00.2163/examples/01_standard  
RUN mpirun --allow-run-as-root -x LD_PRELOAD=/usr/lib64/openmpi/lib/libmpi.so
-np 4 ../../bin/lnx/flow2d3d/bin/d_hydro.exe ./config_flow2d3d.xml  

