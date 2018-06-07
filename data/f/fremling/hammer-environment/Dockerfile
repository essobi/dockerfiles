# This docke-build will seetup the environment needed to build the  
# hammer software.  
FROM ubuntu:14.04  
MAINTAINER Mikael Fremling <micke.fremling@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
##install all the python utilities  
RUN apt-get update  
RUN apt-get install -y python-software-properties software-properties-common
build-essential  
##Install the petc-slepc packages  
#####RUN apt-add-repository ppa:niall-moran/hammer  
##RUN apt-get update  
######RUN apt-get install -y python-petsc4py python-slepc4py  
###Install python pip, blas and other nececarry things.  
RUN apt-get install -y python-pip python-dev libhdf5-dev libopenmpi-dev
liblapack-dev libblas-dev gfortran  
  
RUN python -m pip install --upgrade pip  
RUN pip install cython numpy scipy matplotlib  
###RUN apt-get install -y python-cython python-numpy python-matplotlib git  
###Build PETc, SLEPc, PETc4py, SLEPc4py  
###Download PETc  
ADD http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-3.7.5.tar.gz
petsc-3.7.5.tar.gz  
###Download PETc4py  
ADD https://bitbucket.org/petsc/petsc4py/downloads/petsc4py-3.7.0.tar.gz
petsc4py-3.7.0.tar.gz  
###Download SLEPc  
ADD http://slepc.upv.es/download/download.php?filename=slepc-3.7.3.tar.gz
slepc-3.7.3.tar.gz  
###Download SLEPc4py  
ADD https://bitbucket.org/slepc/slepc4py/downloads/slepc4py-3.7.0.tar.gz
slepc4py-3.7.0.tar.gz  
  
###Extract the catalouges  
RUN tar -xzvf petsc-3.7.5.tar.gz  
RUN tar -xzvf petsc4py-3.7.0.tar.gz  
RUN tar -xzvf slepc-3.7.3.tar.gz  
RUN tar -xzvf slepc4py-3.7.0.tar.gz  
  
### ----------Install PETc-----  
WORKDIR /petsc-3.7.5  
ENV PETSC_DIR /petsc-3.7.5  
ENV PETSC_ARCH linux-gnu-cxx-complex  
RUN ./configure --with-clanguage=C++ --with-cxx-support=1 --with-gcov=1
--with-scalar-type=complex --with-shared-libraries=1 --with-debugging=0
--with-scientific-python=1  
RUN make PETSC_DIR=$PETSC_DIR PETSC_ARCH=$PETSC_ARCH all  
RUN make PETSC_DIR=$PETSC_DIR PETSC_ARCH=$PETSC_ARCH test  
  
### ----------Install SLEPc-----  
WORKDIR /slepc-3.7.3  
RUN ./configure  
ENV SLEPC_DIR /slepc-3.7.3  
RUN make SLEPC_DIR=$SLEPC_DIR PETSC_DIR=$PETSC_DIR PETSC_ARCH=$PETSC_ARCH  
RUN make SLEPC_DIR=$SLEPC_DIR PETSC_DIR=$PETSC_DIR PETSC_ARCH=$PETSC_ARCH test  
  
### ----------Install PETc4py-----  
WORKDIR /petsc4py-3.7.0  
RUN python setup.py build  
RUN PETSC_DIR=$PETSC_DIR PETSC_ARCH=$PETSC_ARCH python setup.py install  
  
### ----------Install SLEPc4py-----  
WORKDIR /slepc4py-3.7.0  
### Replace a file that has a bug while building under compex cpp  
ADD
https://bitbucket.org/slepc/slepc4py/raw/a93f720cf03e48aa9bb84283d7b2f5423d0b6cfa/src/SLEPc/BV.pyx
/slepc4py-3.7.0/BV_new.pyx  
RUN cp -v BV_new.pyx src/SLEPc/BV.pyx  
###remove the slepc4py.SLEPc.c file since it is prepuilt wrongly now  
RUN rm src/slepc4py.SLEPc.c  
###Run the build  
RUN python setup.py build  
RUN PETSC_DIR=$PETSC_DIR PETSC_ARCH=$PETSC_ARCH SLEPC_DIR=$SLEPC_DIR python
setup.py install  
  
###Utilities for the diagonalizer build into the CFT-catalouge  
RUN apt-get install -y libarpack2-dev  
  
# Install the utulitie needed for building the documentation  
RUN pip install sphinx==1.4.8 sphinx_rtd_theme recommonmark  
  
##Install the FQHE untilities for the sphere  
RUN apt-get install -y libgsl0-dev  
  
# Finish of by installing some lightwight software  
RUN apt-get install -y hdf5-tools git emacs bc octave  
  
###Return to root  
WORKDIR /  

